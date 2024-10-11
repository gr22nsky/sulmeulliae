from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from evaluations.models import Evaluation, Review 
from .chatgpt import summarize_review

class SummaryAPIView(APIView):
    def post(self, request, evaluation_id):
        from chatgpt.models import Summary
        try:
            evaluation = Evaluation.objects.get(id=evaluation_id)
            reviews = evaluation.reviews.all()

            if not reviews:
                return Response({"error": "No reviews found for this evaluation."}, status=status.HTTP_404_NOT_FOUND)

            # 모든 리뷰 내용을 하나의 문자열로 합치기
            all_reviews_content = "\n".join(review.content for review in reviews)

            # 전체 리뷰를 요약
            summary_content = summarize_review(all_reviews_content)
    
            # Summary 모델에 저장
            summary = Summary(evaluation=evaluation, summary_content=summary_content)
            summary.save()

            return Response({"summary": summary_content}, status=status.HTTP_201_CREATED)

        except Evaluation.DoesNotExist:
            return Response({"error": "Evaluation not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

