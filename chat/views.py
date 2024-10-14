from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .models import ChatRoom
from .serializers import ChatRoomSerializer
from django.shortcuts import get_object_or_404
from urllib.parse import unquote

class CreateChatRoomAPIView(APIView):
    def post(self, request):
        user = request.user
        room_name = request.data.get('name')
        if not room_name:
            return Response({"error": "Room name is required"}, status=status.HTTP_400_BAD_REQUEST)
        chatroom = ChatRoom.objects.create(name=room_name, created_by=user)
        serializer = ChatRoomSerializer(chatroom)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ChatRoomListAPIView(ListAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer

class ChatRoomDetailAPIView(APIView):
    def get(self, request, room_id):
        chatroom = get_object_or_404(ChatRoom, id=room_id)
        serializer = ChatRoomSerializer(chatroom)
        return Response(serializer.data)

class DeleteChatRoomAPIView(APIView):
    def delete(self, request, room_id):
        # 채팅방이 존재하는지 확인
        chatroom = get_object_or_404(ChatRoom, id=room_id)
        # 방을 생성한 사용자인지 확인
        if chatroom.created_by != request.user:
            return Response({"error": "You are not allowed to delete this room."}, status=status.HTTP_403_FORBIDDEN)
        
        # 방 삭제
        chatroom.delete()
        return Response({"message": "Chat room deleted successfully"}, status=status.HTTP_204_NO_CONTENT)