import requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from evaluations.models import Evaluation
from .models import Suggestion
from .chatbot import sulmeulliae_bot

class ChatBotAPIView(APIView):

    def translate_text(self, text, target_lang):

        url= "https://api-free.deepl.com/v2/translate" 
        params = {
            'auth_key': settings.DEEPL_API_KEY,
            'text': text,
            'target_lang': target_lang
        }

        response = requests.post(url, data=params)
        response_data = response.json()

        if 'translations' in response_data:
            return response_data['translations'][0]['text']
        else:
            return Response({
                "Translation error:": + response_data.get('message', 'Unknown error')
            }, status=400)

    def post(self, request):
        
        liquors = []
        for evaluation in Evaluation.objects.all():  # Evaluation 모델에서 모든 객체 가져오기
            liquors.append(evaluation.title)

        user = request.user  # 현재 로그인된 사용자
        data = request.data
        message = data.get("message", "") 

        # 포인트 확인
        if user.points > 0:
            user.points -= 1  # 1포인트 차감 
            user.save()
            
            message_transleat = self.translate_text(message,'EN')

            # 챗봇 로직 호출
            sulmeulliae_message = self.translate_text(sulmeulliae_bot(message_transleat,liquors),'KO')

            suggestion = Suggestion.objects.create(
                suggestion = sulmeulliae_message,
                feeling = data.get("message", "")
            )

            return Response({
                "sulmeulliae_message": sulmeulliae_message,
                "points": user.points  # 남은 포인트도 응답에 포함
            })
        else:
            # 포인트가 0인 경우
            return Response({
                "error": "포인트가 부족합니다."
            }, status=403)