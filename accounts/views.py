from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import User
from .validators import validate_user_data
from .serializers import UserSerializer
import requests


class UserCreateView(APIView):
    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny()]
        return [IsAuthenticated()]
    
    def post(self, request):
        rlt_message = validate_user_data(request.data)
        if rlt_message is not None:
            return Response(
                {"message":rlt_message},
                status=400)
        
        user = User.objects.create_user(**request.data)
        
        refresh = RefreshToken.for_user(user) #토큰 발급
        
        serializer = UserSerializer(user)
        response_dict = serializer.data
        response_dict["access"] = str(refresh.access_token),
        response_dict["refresh"] = str(refresh)
        return Response(response_dict)

        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    #회원 탈퇴
    def delete(self, request):
        old_password = request.data.get("old_password")
        if not request.user.check_password(old_password):
            return Response(
                {"message":"기존 비밀번호가 일치하지 않습니다."},
                status=400)
        request.user.delete()
        return Response(status=204)
        
    #회원 정보 수정       
    def put(self, request):
        user = request.user
        
        nickname = request.data.get("nickname")
        profile_images = request.data.get("profile_images")

        if nickname:
            user.nickname = nickname
        if profile_images:
            user.profile_image = profile_images    
        user.save()
        serializer = UserSerializer(user)
        return Response(
            {"message":"회원 정보가 성공적으로 수정되었습니다.",
            "user":serializer.data},
            status=200)
    
    
class UserSigninView(APIView):
    
    permission_classes = [AllowAny]
    
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        
        user = authenticate(username=username, password=password)
        if not user:
            return Response(
                {"message":"로그인 정보가 일치하지 않습니다."},
                status=400)
        refresh = RefreshToken.for_user(user)
        return Response(
            {'refresh': str(refresh),
            'access': str(refresh.access_token)})

        
class UserProfileView(APIView):
    def get(self, request, username):
        #유저조회
        user = User.objects.get(username=username)
        #User 객체 직렬화(JSON)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    

class UserSignoutView(APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh')
    
        if not refresh_token: 
            return Response(
                {"message":"리프레시 토큰이 필요합니다"}, 
                status=400)
    
        try:
            token = OutstandingToken.objects.get(token=refresh_token)
            BlacklistedToken.objects.create(token=token)
        except OutstandingToken.DoesNotExist:
            return Response(
                {"detail": "유효하지 않은 리프레시 토큰입니다."}, 
                status=400)
        return Response(
            {"detail": "로그아웃 성공"}, 
            status=205)    
    

class UserPasswordUpdateView(APIView):
    def post(self, request):
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        
        if not request.user.check_password(old_password):
            return Response(
                {"message":"기존 비밀번호가 일치하지 않습니다."},
                status=400)
        
        request.user.set_password(new_password)
        request.user.save()
        return Response(
            {"message": "비밀번호가 성공적으로 변경되었습니다."},
            status=200)