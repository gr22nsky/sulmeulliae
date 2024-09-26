from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from .models import User
from .validators import validate_user_data
from .serializers import UserSerializer


class UserCreateView(APIView):
    
    permission_classes = [AllowAny]
    
    def post(self, request):
        rlt_message = validate_user_data(request.data)
        if rlt_message is not None:
            return Response({"message":rlt_message},status=400)
        
        user = User.objects.create_user(**request.data)
        return Response({"message":"가입을 환영합니다."},status=200)

        
class UserSigninView(APIView):
    
    permission_classes = [AllowAny]
    
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        
        user = authenticate(username=username, password=password)
        if not user:
            return Response(
                {"message":"일치하는 회원이 존재하지 않습니다."},
                            status=400,
                            )
        
        
        refresh = RefreshToken.for_user(user)
        return Response (
            {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            }
        )
        
class UserProfileView(APIView):
    
    def get(self, request, username):
        #유저조회
        user = User.objects.get(username=username)
        #User 객체 직렬화(JSON)
        serializer = UserSerializer(user)
        return Response(serializer.data)