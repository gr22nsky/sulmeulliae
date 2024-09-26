from rest_framework import serializers
from .models import Community, Comment, Image, Category


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ("id", "category")


class ImageSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(use_url=True)

    class Meta:
        model = Image
        fields = (
            "id",
            "image_url",
        )


class CommunityListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    like_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Community
        fields = (
            "id", 
            "title",
            "author",
            "view_count",
            "like_count",
        )

    def get_like_count(self, obj):
        return obj.like.count()

class CommunityCreateSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField(read_only=True)
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Community
        fields = (
            "id",
            "title",
            "category",
            "content",
            "images",
            "author",
            "view_count",
        )
        write_only_fields = ("content",)

    def get_images(self, instance):
        if instance.images.exists():
            return list(
                instance.images.values_list("image_url", flat=True)
            )  # 이미지 URL 반환
        return None  