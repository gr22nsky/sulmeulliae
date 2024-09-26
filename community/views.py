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
    CommunityDetailSerializer,
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


# 커뮤니티 세부 조회 수정 및 삭제
class CommunityDetailAPIView(UpdateAPIView):
    queryset = Community.objects.filter(is_deleted=False)
    serializer_class = CommunityListSerializer
    pagination_class = CommunityPagination
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        community= get_object_or_404(Community, pk=pk)
        user = request.user
        serializer = CommunityDetailSerializer(community)
        return Response(serializer.data, status=200)

    # 이미지 수정 로직
    def perform_update(self, serializer):
        images_data = self.request.FILES.getlist('images')
        instance = serializer.instance  # 현재 수정 중인 기사 객체

        # 요청에 이미지가 포함된 경우
        if images_data:
            # 기존 이미지 삭제
            instance.images.all().delete()
            for image_data in images_data:
                Image.objects.create(article=instance, image_url=image_data)

        serializer.save()

    def delete(self, request, pk):
        article = get_object_or_404(Community, pk=pk)
        self.check_object_permissions(request, article)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)