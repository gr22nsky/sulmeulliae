from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Size(models.Model):
    size = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.size

class Origin(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Evaluation(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='evaluation')
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='evaluation')
    content = models.TextField()
    image = models.ImageField(upload_to='images/evaluation', blank=True)
    ABV = models.IntegerField()
    hit = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 중계테이블에서 가져오기
    size = models.ManyToManyField(Size, symmetrical=False, related_name='evaluation')
    origin = models.ManyToManyField(Origin, symmetrical=False, related_name='evaluation')
    ingredient = models.ManyToManyField(Ingredient, symmetrical=False, related_name='evaluation')

    def __str__(self):
        return self.title
    
class Review(models.Model):
    ratings = [
        ('5', '★★★★★'),
        ('4', '★★★★'),
        ('3', '★★★'),
        ('2', '★★'),
        ('1', '★'),
        ('0', '☆')
    ]
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField()
    rating = models.CharField(max_length=1, choices=ratings)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

