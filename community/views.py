from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,UpdateAPIView
from rest_framework.permissions import (IsAuthenticated, AllowAny,IsAdminUser)

from .paginatuions import CommunityPagination
from .models import Community, Comment, Image, Category
from .serializers import (
    CommunityListSerializer,
    CommunityCreateSerializer,
)

#커뮤니티 게시글 생성 및 리스트 조회
class CommunityListAPIView(ListCreateAPIView):
    queryset = Community.objects.filter(is_deleted=False)
    serializer_class = CommunityListSerializer
    pagination_class = CommunityPagination
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
            self.permission_classes = [AllowAny]
            return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.serializer_class = CommunityCreateSerializer
        images = request.FILES.getlist("images")
        if not images:  
            return Response({"ERROR": "Image file is required."}, status=400)
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        images = self.request.FILES.getlist("images")
        community = serializer.save(author=self.request.user)
        for image in images:
            Image.objects.create(community=community, image_url=image)