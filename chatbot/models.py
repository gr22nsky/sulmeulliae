from django.db import models

class Suggestion(models.Model):
    suggestion=models.TextField(max_length=255)
    feeling = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
