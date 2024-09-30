from django.contrib import admin
from accounts.models import User
from .models import Category, Community, Comment,Image

# Register your models here.

class CommunityAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at']
    list_filter = ['category']
    search_fields = ['title', 'content']

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Community)
admin.site.register(Comment)
admin.site.register(Image)
