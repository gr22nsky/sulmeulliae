from django.contrib import admin
from .models import Product, Order, Cart, CartItem


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock")  # 목록에서 보여줄 필드
    search_fields = ("name",)  # 검색 가능 필드


admin.site.register(Product, ProductAdmin)  # Product 모델 등록
admin.site.register(Order)  # Order 모델 등록
admin.site.register(Cart)  # Cart 모델 등록
admin.site.register(CartItem)  # CartItem 모델 등록
