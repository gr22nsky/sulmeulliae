from rest_framework import serializers
from . import models

class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = models.EvaluationImage
        fields = (
            "image",
        )
        
class EvaluationSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    like_count = serializers.SerializerMethodField()
    class Meta:
        model = models.Evaluation
        fields = (
            'title',
            'category',
            'content',
            'size',
            'origin',
            'ABV',
            'ingredient',
            'avg_rating',
            'viewcounts',
            'like_count',
            'images',
        )
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if instance.category:
            ret['category'] = instance.category.name
        ret['size'] = [size.size for size in instance.size.all()]
        ret['origin'] = [origin.name for origin in instance.origin.all()]
        ret['ingredient'] = [ingredient.name for ingredient in instance.ingredient.all()]
        return ret
    def get_like_count(self, obj):
        return obj.likes.count()

class ReviewSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()
    class Meta:
        model = models.Review
        fields = (
            'evaluation',
            'author',
            'content',
            'rating',
            'like_count',
            'updated_at',
        )
        read_only_fields = ('evaluation', 'author')
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['evaluation'] = instance.evaluation.title
        ret['author'] = instance.author.username
        return ret
    
    def get_like_count(self, obj):
        return obj.likes.count()