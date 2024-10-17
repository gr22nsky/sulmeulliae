from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.conf import settings
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Evaluation, Review, ReviewSummary
from .serializers import EvaluationSerializer, ReviewSerializer
from datetime import timedelta
import requests


# Create your views here.
class EvaluationListAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        evaluations = Evaluation.objects.all()
        # 정렬
        sort = request.GET.get("sort")
        if sort == "like":
            evaluations = evaluations.order_by("-like_count", "-created_at")
        elif sort == "viewcounts":
            evaluations = evaluations.order_by("-viewcounts", "-created_at")
        elif sort == "rating":
            evaluations = evaluations.order_by("-avg_rating", "-created_at")
        else:
            evaluations = evaluations.order_by("-created_at")
        # 검색
        search_query = request.GET.get("search")
        if search_query:
            evaluations = evaluations.filter(
                Q(title__icontains=search_query) | Q(content__icontains=search_query)
            )
        # 페이지네이션
        page = request.GET.get("page", 1)  # 기본값을 1로 설정
        paginator = Paginator(evaluations, 10)
        evaluations = paginator.page(page)
        if not evaluations:
            return Response({"해당하는 평가가 없습니다."}, status=404)

        serializer = EvaluationSerializer(evaluations, many=True)
        return Response(serializer.data)


class EvaluationDetailAPIView(APIView):
    def get(self, request, pk):
        evaluation = get_object_or_404(Evaluation, pk=pk)
        evaluation.viewcounts += 1
        evaluation.save(update_fields=["viewcounts"])
        serializer = EvaluationSerializer(evaluation)
        return Response(serializer.data)


class EvaluationLikeAPIView(APIView):
    def post(self, request, pk):
        evaluation = get_object_or_404(Evaluation, pk=pk)
        user = request.user
        if evaluation.likes.filter(pk=user.pk).exists():
            evaluation.likes.remove(user)
            result = 204
        else:
            evaluation.likes.add(user)
            result = 200

        evaluation.like_count = evaluation.likes.count()
        evaluation.save(update_fields=["like_count"])
        return Response(status=result)


class UserLikedEvaluationAPIView(APIView):
    def get(self, request):
        user = request.user
        evaluations = user.like_evaluation.all()
        serializer = EvaluationSerializer(evaluations, many=True)
        return Response(serializer.data)


class ReviewListAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Evaluation, pk=pk)

    def get(self, request, pk):
        user = request.user
        evaluation = self.get_object(pk=pk)
        reviews = evaluation.reviews.all().exclude(author__in=user.blinded_user.all())

        # 정렬
        sort = request.GET.get("sort")
        if sort == "like":
            reviews = reviews.order_by("-like_count", "-created_at")
        else:
            reviews = reviews.order_by("-created_at")
        # 페이지네이션
        page = request.GET.get("page", 1)  # 기본값을 1로 설정
        paginator = Paginator(reviews, 10)
        reviews = paginator.page(page)
        if not reviews:
            return Response({"해당하는 리뷰가 없습니다."}, status=404)

        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        evaluation = self.get_object(pk=pk)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(evaluation=evaluation, author=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ReviewDetailAPIView(APIView):
    def get(self, request, pk):
        user = request.user
        review = get_object_or_404(
            Review.objects.filter(pk=pk).exclude(author__in=user.blinded_user.all())
        )
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def put(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        serializer = ReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        if review.author != request.user:
            return Response({"작성자만 리뷰를 삭제할수있습니다."}, status=403)
        review.delete()
        return Response(status=204)


class ReviewSummaryAPIView(APIView):
    def translate_text(self, text, target_lang):

        url = "https://api-free.deepl.com/v2/translate"
        params = {
            "auth_key": settings.DEEPL_API_KEY,
            "text": text,
            "target_lang": target_lang,
        }

        response = requests.post(url, data=params)
        response_data = response.json()

        if "translations" in response_data:
            return response_data["translations"][0]["text"]
        else:
            return Response(
                {"Translation error:": +response_data.get("message", "Unknown error")},
                status=400,
            )

    def post(self, request, pk):
        reviews = []
        evaluation = get_object_or_404(Evaluation, pk=pk)

        # 평가에 연결된 모든 리뷰를 내용 추가
        for review in evaluation.reviews.all().order_by("-like_count", "-created_at")[
            :100
        ]:
            reviews.append(review.content)
        # 리뷰를 영어로 번역
        reviews_translation = self.translate_text(" ".join(reviews), "EN")
        summary = self.summarize_reviews(reviews_translation)
        print(summary)
        # 요약을 한국어로 번역
        summary_translation = self.translate_text(summary, "KO")

        # 기존 요약 가져오기 또는 생성
        review_summary, created = ReviewSummary.objects.get_or_create(
            evaluation=evaluation
        )

        # 3개월이 지났으면 요약 갱신
        if not created and (timezone.now() - review_summary.updated_at) > timedelta(
            days=90
        ):
            review_summary.summary = summary_translation
            review_summary.save()
            return Response(
                {"summary": summary_translation, "updated": True}, status=200
            )

        # 처음 생성된 경우
        if created:
            review_summary.summary = summary_translation
            review_summary.save()
            return Response(
                {"summary": summary_translation, "created": True}, status=200
            )

        # 이미 최신 요약이 있는 경우
        return Response(
            {"summary": review_summary.summary, "updated": False}, status=200
        )

    def summarize_reviews(self, reviews):
        api_key = settings.OPENAI_API_KEY
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }

        data = {
            "model": "gpt-4-turbo",
            "messages": [
                {
                    "role": "user",
                    "content": """Summarize the overall description of the following reviews. 
                    Summarize in 3 to 4 sentences in a polite and concise manner, 
                    using natural sentence flow.: """
                    + " ".join(reviews),
                }
            ],
            "max_tokens": 200,
        }

        response = requests.post(
            "https://api.openai.com/v1/chat/completions", headers=headers, json=data
        )
        return response.json()["choices"][0]["message"]["content"]


class ReviewLikeAPIView(APIView):
    def post(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        user = request.user

        if review.likes.filter(pk=user.pk).exists():
            review.likes.remove(user)
            result = 204
        else:
            review.likes.add(user)
            result = 200

        review.like_count = review.likes.count()
        review.save(update_fields=["like_count"])
        return Response(status=result)


class UserLikedReviewAPIView(APIView):
    def get(self, request):
        user = request.user
        reviews = user.like_review.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
