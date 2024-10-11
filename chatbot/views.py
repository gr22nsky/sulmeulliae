from rest_framework.views import APIView
from rest_framework.response import Response
from .chatbot import sulmeulliae_bot


class ChatBotAPIView(APIView):
    def post(self, request):
        user = request.user  # 현재 로그인된 사용자
        data = request.data
        message = data.get("message", "")
        
        # 포인트 확인
        if user.points > 0:
            user.points -= 1  # 1포인트 차감
            user.save()
            
            # 챗봇 로직 호출
            sulmeulliae_message = sulmeulliae_bot(message)
            return Response({
                "sulmeulliae_message": sulmeulliae_message,
                "points": user.points  # 남은 포인트도 응답에 포함
            })
        else:
            # 포인트가 0인 경우
            return Response({
                "error": "포인트가 부족합니다."
            }, status=403)