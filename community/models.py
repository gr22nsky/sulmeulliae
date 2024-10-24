from django.db import models
from django.contrib.auth import get_user_model


class Category(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category


class Community(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="community_author"
    )
    content = models.TextField()
    view_count = models.PositiveIntegerField(blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(
        get_user_model(), related_name="community_like", blank=True
    )
    like_count = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()


class Image(models.Model):
    community = models.ForeignKey(
        Community, on_delete=models.CASCADE, related_name="community_image"
    )
    image_url = models.ImageField(upload_to="images/")


class Comment(models.Model):
    community = models.ForeignKey(
        Community, on_delete=models.CASCADE, related_name="comment_community"
    )
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="comment_author"
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    likes = models.ManyToManyField(
        get_user_model(), related_name="comment_like", blank=True
    )
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.content

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()
