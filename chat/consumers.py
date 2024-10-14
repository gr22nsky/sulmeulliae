import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"

        # 그룹에 가입
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # 그룹에서 탈퇴
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)

        # 'username' 필드를 안전하게 처리
        username = text_data_json.get('username') 
        message = text_data_json.get('message')

        # 받은 메시지를 방의 모든 클라이언트에게 전송
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username  # 시스템 메시지나 일반 메시지에서 사용
            }
        )


    # 방의 클라이언트에게 메시지를 전송
    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        # 메시지를 클라이언트로 전송
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))
