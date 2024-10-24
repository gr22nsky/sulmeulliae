from django.shortcuts import get_object_or_404
from .serializers import UserSerializer, UserProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.token_blacklist.models import (
    BlacklistedToken,
    OutstandingToken,
)
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import (
    UserSerializer,
    UserProfileSerializer,
    LikedEvaluationSerializer,
    LikedReviewSerializer,
    LikedCommunitySerializer,
    LikedCommentSerializer,
)
from django.utils import timezone
from datetime import timedelta
from evaluations.models import Evaluation, Review
from community.models import Community, Comment
from .serializers import UserSerializer, UserProfileSerializer
from django.contrib.auth.tokens import (
    default_token_generator as account_activation_token,
)
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str


class UserAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_dict = {
                "message": "이메일 인증 메일이 발송되었습니다. 이메일을 확인해 주세요."
            }
            return Response(response_dict, status=201)
        return Response(serializer.errors, status=400)

    # 회원 탈퇴
    def delete(self, request):
        password = request.data.get("password")
        if not request.user.check_password(password):
            return Response(
                {"message": "기존 비밀번호가 일치하지 않습니다."}, status=400
            )
        request.user.soft_delete()
        return Response({"message": "회원탈퇴가 완료되었습니다."}, status=204)

    # 회원 정보 수정
    def put(self, request):
        user = request.user
        nickname = request.data.get("nickname")
        profile_image = request.FILES.get("profile_image")
        if nickname:
            user.nickname = nickname
        if profile_image:
            user.profile_image = profile_image
        user.save()
        serializer = UserProfileSerializer(user)
        return Response(
            {
                "message": "회원 정보가 성공적으로 수정되었습니다.",
                "user": serializer.data,
            },
            status=200,
        )


class VerifyEmailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
            if account_activation_token.check_token(user, token):
                user.is_active = True  # 이메일 인증 시 활성화
                user.is_email_verified = True  # 이메일 인증
                user.save()
                return Response(
                    {"message": "이메일 인증이 완료되었습니다!"}, status=200
                )
            else:
                return Response({"error": "인증 토큰이 유효하지 않습니다!"}, status=400)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
            return Response({"error": "잘못된 요청입니다!"}, status=400)


class UserSigninAPIView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if not user:
            return Response(
                {"message": "아이디 또는 비밀번호를 잘못 입력했습니다."}, status=400
            )
        refresh = RefreshToken.for_user(user)
        if user is not None:
            # 마지막 로그인 시간이 24시간 이상 차이가 나면 포인트 지급
            if user.last_login is None or (
                timezone.now() - user.last_login
            ) > timedelta(hours=24):
                user.points += 3  # 3포인트 추가
                user.save()
        user.last_login = timezone.now()
        user.save(update_fields=["last_login"])
        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user_id": user.id,
            }
        )


class UserProfileAPIView(APIView):

    def get(self, request, username):
        user = get_object_or_404(User, username=username, is_active=True)
        if request.user != user:
            return Response({"message": "유저정보는 본인의 것만 확인할 수 있습니다"}, status=401)
        # User 객체 직렬화(JSON)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)

    def post(self, request, username):
        user = get_object_or_404(User, username=username, is_active=True)
        if request.user == user:
            return Response({"message": "자신을 팔로우 할 수 없습니다."}, status=400)
        if not request.user.followings.filter(id=user.id).exists():
            request.user.followings.add(user)
            return Response({"message": "팔로우 하였습니다."}, status=200)
        else:
            request.user.followings.remove(user)
            return Response({"message": "언팔로우 하였습니다."}, status=200)


class UserInfoView(APIView):
    def get(self, request):
        user = request.user
        return Response(
            {
                "username": user.username,
            }
        )


class UserSignoutAPIView(APIView):
    def post(self, request):
        refresh_token = request.data.get("refresh")

        if not refresh_token:
            return Response({"message": "리프레시 토큰이 필요합니다"}, status=400)

        try:
            token = OutstandingToken.objects.get(token=refresh_token)
            BlacklistedToken.objects.create(token=token)
        except OutstandingToken.DoesNotExist:
            return Response(
                {"detail": "유효하지 않은 리프레시 토큰입니다."}, status=400
            )
        return Response({"detail": "로그아웃 성공"}, status=205)


class UserPasswordUpdateAPIView(APIView):
    def post(self, request):
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")

        if not request.user.check_password(old_password):
            return Response(
                {"message": "기존 비밀번호가 일치하지 않습니다."}, status=400
            )

        request.user.set_password(new_password)
        request.user.save()
        return Response(
            {"message": "비밀번호가 성공적으로 변경되었습니다."}, status=200
        )


class BlindAPIView(APIView):

    def post(self, request, username):
        blinded = get_object_or_404(User, username=username)
        user = request.user
        if blinded == user:
            return Response({"message": "잘못된 접근입니다."}, status=403)

        if blinded in user.blinded_user.all():
            user.blinded_user.remove(blinded)
            return Response(
                {"message": f" {username}을 블라인딩 해제 하셨습니다."}, status=200
            )

        user.blinded_user.add(blinded)
        return Response({"message": f" {username}을 블라인딩 하셨습니다."}, status=200)


class UserLikesAPIView(APIView):
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        if request.user != user:
            return Response({"message": "유저정보는 본인의 것만 확인할 수 있습니다"}, status=401)

        liked_evaluations = Evaluation.objects.filter(likes=user)
        liked_reviews = Review.objects.filter(likes=user)
        liked_communities = Community.objects.filter(likes=user)
        liked_comments = Comment.objects.filter(likes=user)

        evaluations_serializer = LikedEvaluationSerializer(liked_evaluations, many=True)
        reviews_serializer = LikedReviewSerializer(liked_reviews, many=True)
        communities_serializer = LikedCommunitySerializer(liked_communities, many=True)
        comments_serializer = LikedCommentSerializer(liked_comments, many=True)

        return Response(
            {
                "liked_evaluations": evaluations_serializer.data,
                "liked_reviews": reviews_serializer.data,
                "liked_communities": communities_serializer.data,
                "liked_comments": comments_serializer.data,
            }
        )
#confirm
