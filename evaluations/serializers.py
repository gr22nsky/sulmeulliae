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
    class Meta:
        model = models.Evaluation
        fields = '__all__'
        
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if instance.category:
            ret['category'] = instance.category.name
        ret['size'] = [size.size for size in instance.size.all()]
        ret['origin'] = [origin.name for origin in instance.origin.all()]
        ret['ingredient'] = [ingredient.name for ingredient in instance.ingredient.all()]
        ret.pop('id')
        ret.pop('author')
        ret.pop('created_at')
        ret.pop('updated_at')
        return ret
    

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'
        read_only_fields = ('evaluation', 'author')

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['evaluation'] = instance.evaluation.title
        ret['author'] = instance.author.username
        ret.pop('id')
        ret.pop('evaluation')
        ret.pop('created_at')
        return ret