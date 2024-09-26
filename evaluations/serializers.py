from rest_framework import serializers
from . import models

class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Evaluation
        exclude = ['id','author','created_at','updated_at']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.category:
            representation['category'] = instance.category.name
        representation['size'] = [size.size for size in instance.size.all()]
        representation['origin'] = [origin.name for origin in instance.origin.all()]
        representation['ingredient'] = [ingredient.name for ingredient in instance.ingredient.all()]

        return representation