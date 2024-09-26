from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .validators import validate_user_data
from .serializers import UserSerializer


class UserCreateView(APIView):
    def post(self, request):
        rlt_message = validate_user_data(request.data)
        if rlt_message is not None:
            return Response({"message":rlt_message},status=400)

        user = User.objects.create_user(**request.data)
        
        serializer = UserSerializer(user)
        return Response(serializer.data)

