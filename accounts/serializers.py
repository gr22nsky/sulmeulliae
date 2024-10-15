from .utils import send_verification_email
from .models import User
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from . import views

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "fullname", "nickname", "birth", "email", "points",)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(("이 이메일은 이미 사용 중입니다."))
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.is_email_verified = False
        user.save()
        send_verification_email(user)  # 이메일 인증 메일 전송
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "fullname", "nickname", "birth", "email", "profile_image", "points",)
