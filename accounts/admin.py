from django.contrib import admin
from .models import User
from community.models import Category, Community, Comment

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Community)
admin.site.register(Comment)