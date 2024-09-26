from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User



class UserCreateView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        fullname = request.data.get("fullname")
        nickname = request.data.get("nickname")
        email = request.data.get("email")
        birth = request.data.get("birth")
        
        birth_year = int(birth.split('-')[0])
        
        if birth_year > 2005:
            return Response({"message":"가입불가 미성년자입니다"},
                            status=400)

        return Response({"message":"가입을 환영합니다"})
        
        
        user = User.objects.create_user(
            
            username=username,
            password=password,
            fullname=fullname,
            nickname=nickname,
            email=email,
            birth=birth,
            
        )
        

        

