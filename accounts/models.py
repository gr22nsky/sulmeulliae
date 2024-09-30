from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    first_name = None
    last_name = None
    fullname = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    birth = models.DateField(null=True)
    adult_verification = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True)
    
    def __str__(self):
        return self.username
    
    def soft_delete(self):
        self.is_active = False
        self.save()