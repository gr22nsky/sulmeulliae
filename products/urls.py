from django.conf.urls.static import static
from django.urls import path
from backend import settings
from .views import (
    ProductListView,
    ProductDetailView,
    CartView,
    KakaoPayCartReadyView,
    KakaoPayCartApproveView, UserOrderItemsView,
)

urlpatterns = [
    path("", ProductListView.as_view(), name="product-list"),
    path("<uuid:product_id>/", ProductDetailView.as_view(), name="product-detail"),
    path("cart/", CartView.as_view(), name="cart"),
    path("cart/<int:item_id>/", CartView.as_view(), name="cart-delete"),
    path("orders/items/", UserOrderItemsView.as_view(), name="user-order-items"),
    path(
        "payment/kakaopay-cart/ready/",
        KakaoPayCartReadyView.as_view(),
        name="kakao-pay-cart-ready",
    ),
    path(
        "payment/kakaopay-cart/approve/",
        KakaoPayCartApproveView.as_view(),
        name="kakao-pay-cart-approve",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



