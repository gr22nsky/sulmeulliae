from django.shortcuts import get_object_or_404
from django.db.models import Q

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from .paginations import CommunityPagination, CommentPagination
from .models import Community, Comment, Image, Category
from .serializers import (
    CommunityListSerializer,
    CommunityCreateSerializer,
    CommunityDetailSerializer,
    CommentSerializer,
)


# 커뮤니티 게시글 생성 및 리스트 조회
class CommunityListAPIView(ListCreateAPIView):
    queryset = Community.objects.filter(is_deleted=False)
    serializer_class = CommunityListSerializer
    pagination_class = CommunityPagination

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    # 차단된 사람 제외
    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            community = Community.objects.filter(is_deleted=False).exclude(
                author__in=user.blinded_user.all()
            )
        else:
            community = self.queryset

        # 검색기능
        search_query = request.query_params.get("search", None)
        if search_query:
            community = community.filter(
                Q(title__icontains=search_query)
                | Q(author__username__icontains=search_query)
                | Q(content__icontains=search_query)
            )
        else:
            Response({"messages": "검색결과가 없습니다."}, status=200)

        # 정렬기능
        sort = request.query_params.get("sort", None)

        if sort == "popular":
            community = community.order_by("-view_count")
        elif sort == "title":
            community = community.order_by("title")
        elif sort == "like":
            community = community.order_by("-like_count", "-created_at")
        else:
            community = community.order_by("-created_at")

        self.queryset = community
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.serializer_class = CommunityCreateSerializer
        images = request.FILES.getlist("images")

        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        images = self.request.FILES.getlist("images")
        community = serializer.save(author=self.request.user)
        for image in images:
            Image.objects.create(community=community, image_url=image)


# 커뮤니티 세부 조회 수정 및 삭제
class CommunityDetailAPIView(UpdateAPIView):
    queryset = Community.objects.filter(is_deleted=False)
    serializer_class = CommunityDetailSerializer
    # pagination_class = CommunityPagination

    # 차단된 사람 제외
    def get(self, request, pk):
        user = request.user
        community = get_object_or_404(
            Community.objects.filter(pk=pk, is_deleted=False).exclude(
                author__in=user.blinded_user.all()
            )
        )

        serializer = CommunityDetailSerializer(community)
        return Response(serializer.data, status=200)

    def put(self, request, pk):
        community = get_object_or_404(Community, pk=pk, is_deleted=False)
        author = community.author
        user = request.user
        if user != author:
            return Response({"error": "이 글을 쓴 본인이 아닙니다."}, status=403)

        serializer = CommunityDetailSerializer(
            community, data=request.data, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            self.perform_update(serializer)
            return Response(serializer.data, status=200)
        return Response(status=400)

    # 이미지 수정 로직
    def perform_update(self, serializer):
        instance = serializer.instance
        images_data = self.request.FILES.getlist("images")

        # 요청에 이미지가 포함된 경우
        if images_data:
            # 기존 이미지 삭제
            instance.community_image.all().delete()
            for image_data in images_data:
                Image.objects.create(community=instance, image_url=image_data)
        serializer.save()

    def delete(self, request, pk):
        author = community.author
        user = request.user
        if user != author:
            return Response({"error": "이 글을 쓴 본인이 아닙니다."}, status=403)
        
        community = get_object_or_404(Community, pk=pk)
        self.check_object_permissions(request, community)
        community.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 커뮤니티 좋아요 기능
class CommunityLikeAPIView(APIView):

    def post(self, request, pk):
        community = get_object_or_404(Community, pk=pk, is_deleted=False)

        if request.user in community.likes.all():
            community.likes.remove(request.user)
            result = 204
        else:
            community.likes.add(request.user)
            result = 200

        community.like_count = community.likes.count()
        community.save(update_fields=["like_count"])
        return Response(status=result)


# 유저가 좋아요한 커뮤니티 리스트 조회
class CommunityLikeListAPIView(ListAPIView):
    serializer_class = CommunityListSerializer

    def get_queryset(self):
        user = self.request.user
        return Community.objects.filter(likes=user)


# 댓글 생성 및 리스트 조회
class CommentListAPIView(ListCreateAPIView):
    queryset = Comment.objects.filter(is_deleted=False)
    serializer_class = CommentSerializer
    pagination_class = CommentPagination

    def get(self, request, pk):
        user = self.request.user
        # 차단한 유저가 쓴 커뮤니티는 조회 하지 않음
        community = (
            Community.objects.filter(pk=pk, is_deleted=False)
            .exclude(author__in=user.blinded_user.all())
            .first()
        )
        comments = Comment.objects.filter(community_id=pk, is_deleted=False).exclude(
            author__in=user.blinded_user.all()
        )

        # comments = self.queryset
        serializer = CommentSerializer(comments, many=True)
        정렬기능
        sort = request.query_params.get("sort", None)
        if sort == "like":
            comment = comment.order_by("-like_count")
        else:
            comment = comment.order_by("-created_at")
        self.queryset = comment
        return Response(serializer.data, status=200)

    def post(self, request, pk):
        community = Community.objects.get(pk=pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(community=community, author=self.request.user)
            return Response(serializer.data, status=201)


# 댓글 수정 및 삭제
class CommentEditAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk, is_deleted=False)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=200)

    def put(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk, is_deleted=False)
        author = comment.author
        user = request.user
        if user != author:
            return Response({"error": "이 댓글을 쓴 본인이 아닙니다."}, status=403)
        if not comment:
            return Response({"error": "이 댓글을 찾을 수 없습니다."}, status=404)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(status=400)

    def delete(self, request, pk):
        comment = Comment.objects.filter(pk=pk, is_deleted=False).first()
        author = comment.author
        user = request.user
        if user != author:
            return Response({"error": "이 댓글을 쓴 본인이 아닙니다."}, status=403)
        if not comment:
            return Response({"error": "이 댓글을 찾을 수 없습니다."}, status=404)
        comment.delete()
        return Response({"detail": "댓글이 삭제되었습니다."}, status=204)


# 커뮤니티 댓글 좋아요 기능
class CommentLikeAPIView(APIView):

    def post(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk, is_deleted=False)

        if request.user in comment.likes.all():
            comment.likes.remove(request.user)
            result = 204
        else:
            comment.likes.add(request.user)
            result = 200

        comment.like_count = comment.likes.count()
        comment.save(update_fields=["like_count"])
        return Response(status=result)


# 유저가 좋아요한 댓글 리스트 조회
class CommentLikeListAPIView(ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        user = self.request.user
        return Comment.objects.filter(likes=user)
