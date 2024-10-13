from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from evaluations.models import Evaluation, Review # 데이터베이스에서 평가와 리뷰 정보를 가져오기
from .chatgpt import summarize_review  # 리뷰 내용을 요약하는 기능을 제공하는 함수 가져오기

class SummaryAPIView(APIView):
    def post(self, request, evaluation_id):
        from chatgpt.models import Summary #요약을 저장하기 위해 Summary 모델 가져오기 
        try:
            evaluation = Evaluation.objects.get(id=evaluation_id)
            reviews = evaluation.reviews.all()

            if not reviews:
                return Response({"error": "리뷰가 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

            # 모든 리뷰 내용을 하나의 문자열로 합치기
            all_reviews_content = "\n".join(review.content for review in reviews)

            # 전체 리뷰를 요약
            summary_content = summarize_review(all_reviews_content)
    
            # Summary 모델에 저장
            summary = Summary(evaluation=evaluation, summary_content=summary_content)
            summary.save()

            return Response({"GPT가 리뷰를 요약했어요": summary_content}, status=status.HTTP_201_CREATED)

        except Evaluation.DoesNotExist:
            return Response({"error": "Evaluation not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

