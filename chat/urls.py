from django.urls import path
from . import views

urlpatterns = [
    path('createchat/', views.CreateChatRoomAPIView.as_view(), name='create_chatroom'),
    path('chatrooms/', views.ChatRoomListAPIView.as_view(), name='chat_list'),
    path('chatrooms/<uuid:room_id>/', views.ChatRoomDetailAPIView.as_view(), name='chatroom_detail'),
    path('chatrooms/<uuid:room_id>/delete/', views.DeleteChatRoomAPIView.as_view(), name='delete_chatroom'),
]
