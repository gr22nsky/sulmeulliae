from .models import User
from evaluations.models import Evaluation, Review
from community.models import Community, Comment
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "fullname", "nickname", "birth", "email", "points",)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "fullname", "nickname", "birth", "email", "profile_image","points",)

class LikedEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation  # 평가 모델
        fields = ['id', 'title', 'created_at']

class LikedReviewSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()  # author를 username으로 표시
    evaluation = serializers.CharField(source='evaluation.title')  # 리뷰가 속한 평가 제목 추가
    evaluation_id = serializers.IntegerField(source='evaluation.id')  # 평가 ID 추가
    class Meta:
        model = Review  # 리뷰 모델
        fields = ['id', 'content', 'author', 'evaluation', 'evaluation_id', 'created_at']

class LikedCommunitySerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()  # author를 username으로 표시
    class Meta:
        model = Community  # 커뮤니티 게시물 모델
        fields = ['id', 'title', 'author', 'created_at']

class LikedCommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()  # author를 username으로 표시
    community = serializers.CharField(source='community.title')  # 댓글이 속한 커뮤니티 제목 추가
    community_id = serializers.IntegerField(source='community.id')  # 커뮤니티 ID 추가
    class Meta:
        model = Comment  # 댓글 모델
        fields = ['id', 'content', 'author', 'community', 'community_id', 'created_at']
