from django.db import models
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()
# Create your models here.

class ChatRoom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)  # 한글이나 다른 문자열을 받을 수 있는 필드
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)