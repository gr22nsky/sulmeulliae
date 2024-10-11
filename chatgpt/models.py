from django.db import models
from django.conf import settings
from django.db.models import Avg
from evaluations.models import Evaluation


class Summary(models.Model):
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)  # 원본 댓글과 연관
    summary_content = models.TextField()  # 요약된 내용
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 날짜
    
    def __str__(self):
        return f"{self.review.content[:50]}"