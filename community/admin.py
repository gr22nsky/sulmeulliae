from django.contrib import admin
from accounts.models import User
from .models import Category, Community, Comment,Image

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Community)
admin.site.register(Comment)
admin.site.register(Image)
