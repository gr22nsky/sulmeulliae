from django.contrib import admin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .models import Evaluation, EvaluationImage, ReviewSummary, Review, Category, Size, Origin, Ingredient
from .views import ReviewSummaryAPIView 
from django.contrib import messages


class EvaluationImageAdmin(admin.ModelAdmin):
    list_display = ["image", "evaluation"]
    list_display_links = ["evaluation"]
    search_fields = ["evaluation__title"]


class EvaluationAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "avg_rating", "created_at"]
    list_filter = ["category"]
    search_fields = ["title", "category__name"]

    actions = ["generate_review_summary"]

    def generate_review_summary(self, request, queryset):
        
        review_summary_api = ReviewSummaryAPIView()

        for evaluation in queryset:
            response = review_summary_api.post(request, evaluation.pk)

            if response.status_code == 200:
                summary = response.data.get("summary")
                created_or_updated = (
                    _("생성됨") if response.data.get("created") else _("갱신됨")
                )
                self.message_user(
                    request,
                    f"'{evaluation.title}'에 대한 리뷰 요약이 {created_or_updated}.",
                    messages.SUCCESS,
                )
            else:
                self.message_user(
                    request,
                    f"'{evaluation.title}'의 리뷰 요약 생성에 실패했습니다.",
                    messages.ERROR,
                )

    generate_review_summary.short_description = _("선택된 평가의 리뷰 요약 생성")

admin.site.register(Evaluation, EvaluationAdmin)
admin.site.register(EvaluationImage, EvaluationImageAdmin)
admin.site.register(ReviewSummary) 
admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Origin)
admin.site.register(Ingredient)
admin.site.register(Review)
