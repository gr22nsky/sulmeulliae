from django.contrib import admin

# Register your models here.
from . import models


class EvaluationImageAdmin(admin.ModelAdmin):
    list_display = ["image", "evaluation"]
    list_display_links = ["evaluation"]
    search_fields = ["evaluation__title"]


class EvaluationAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "avg_rating", "created_at"]
    list_filter = ["category"]
    search_fields = ["title", "category__name"]


admin.site.register(models.Evaluation, EvaluationAdmin)
admin.site.register(models.EvaluationImage, EvaluationImageAdmin)
admin.site.register(models.Category)
admin.site.register(models.Size)
admin.site.register(models.Origin)
admin.site.register(models.Ingredient)
admin.site.register(models.Review)
