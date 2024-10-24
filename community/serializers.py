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

    class Meta:
        model = Community
        fields = (
            "id",
            "title",
            "author",
            "view_count",
            "likes",
            "like_count",
            "category",
        )



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
            "likes",
        )
        write_only_fields = ("content",)

    def get_images(self, instance):
        if instance.community_image.exists():
            return list(
                instance.community_image.values_list("image_url", flat=True)
            )  # 이미지 URL 반환
        return None
    

class CommunityDetailSerializer(serializers.ModelSerializer):
    community_image = ImageSerializer(many=True)
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Community
        fields = (
            "id",
            "title",
            "category",
            "content",
            "community_image",
            "author",
            "view_count",
            "like_count",
            "likes",
            "created_at",
            "updated_at",
        )

    def to_representation(self, instance):
        instance.view_count += 1
        instance.save(update_fields=["view_count"])
        return super().to_representation(instance)



class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ("id", "author", "content", "created_at", "updated_at", "like_count", "likes")

