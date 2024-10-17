from rest_framework import serializers
from . import models
from accounts.models import User

class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = models.EvaluationImage
        fields = ("image",)


class EvaluationSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    summary = serializers.SerializerMethodField(default=None)

    class Meta:
        model = models.Evaluation
        fields = (
            "id",
            "title",
            "category",
            "content",
            "size",
            "origin",
            "ABV",
            "ingredient",
            "avg_rating",
            "viewcounts",
            "like_count",
            "likes",
            "images",
            "summary"
        )
    def get_summary(self, obj):
        summary = obj.reviews_summary.all().order_by("-updated_at").first()
        return summary.summary if summary else None

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if instance.category:
            ret["category"] = instance.category.name
        ret["size"] = [size.size for size in instance.size.all()]
        ret["origin"] = [origin.name for origin in instance.origin.all()]
        ret["ingredient"] = [
            ingredient.name for ingredient in instance.ingredient.all()
        ]
        return ret


from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField()  # CharField에서 IntegerField로 변경
    evaluation = serializers.PrimaryKeyRelatedField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = models.Review
        fields = ['id', 'evaluation', 'author', 'content', 'rating', 'likes', 'like_count', 'updated_at']
        extra_kwargs = {
            'likes': {'read_only': True},  # likes 필드가 ManyToMany 관계일 때 read_only 설정
            'evaluation': {'read_only': True},
            'author': {'read_only': True}
        }
