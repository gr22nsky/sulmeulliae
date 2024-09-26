from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Evaluation)
admin.site.register(models.Category)
admin.site.register(models.Size)
admin.site.register(models.Origin)
admin.site.register(models.Ingredient)
admin.site.register(models.Review)