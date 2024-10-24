import uuid
import requests
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    ProductSerializer,
    CartSerializer,
    CartItemSerializer, OrderItemSerializer,
)
from .models import Cart, CartItem, Product, Order, OrderItem
from .utils import get_port_one_token
from django.db import transaction


class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetailView(APIView):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response(
                {"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND
            )


class CartView(APIView):
    def get(self, request):
        try:
            cart = Cart.objects.get(user=request.user)
            serializer = CartSerializer(cart)
            return Response(serializer.data)
        except Cart.DoesNotExist:
            return Response(
                {"error": "Cart not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def post(self, request):
        product_id = request.data.get("product_id")
        quantity = request.data.get("quantity", 1)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response(
                {"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND
            )

        if product.stock < quantity:
            return Response(
                {"error": f"{product.name}의 재고가 부족합니다. (남은 재고: {product.stock})"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, product=product, defaults={"quantity": quantity, "price": product.price * quantity}
        )

        if not created:
            if cart_item.quantity + quantity > product.stock:
                return Response(
                    {"error": f"{product.name}의 재고가 부족합니다."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            cart_item.quantity += quantity
            cart_item.price = product.price * cart_item.quantity
            cart_item.save()

        return Response(
            {"message": "Product added to cart"}, status=status.HTTP_201_CREATED
        )

    def delete(self, request, item_id):
        cart = get_object_or_404(Cart, user=request.user)
        cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)
        serializer = CartItemSerializer(cart_item)
        cart_item.delete()
        return Response(
            {"message": "Product removed from cart", "item": serializer.data},
            status=status.HTTP_204_NO_CONTENT,
        )


class UserOrderItemsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        orders = Order.objects.filter(user=user, is_paid=True)
        if not orders.exists():
            return Response({"message": "구매한 상품이 없습니다."}, status=status.HTTP_404_NOT_FOUND)

        order_items = OrderItem.objects.filter(order__in=orders)
        serializer = OrderItemSerializer(order_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class KakaoPayCartReadyView(APIView):
    def post(self, request):
        order_data = request.data
        products = order_data.get("products", [])
        total_price = 0
        order_items = []

        for item in products:
            product_id = item.get("product_id")
            quantity = item.get("quantity", 1)
            product = get_object_or_404(Product, id=product_id)

            # 재고 확인
            if product.stock < quantity:
                return Response(
                    {
                        "error": f"'{product.name}'의 재고가 부족합니다. 남은 재고: {product.stock}개",
                        "product_id": product_id,
                        "available_stock": product.stock,
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            item_price = product.price * quantity
            total_price += item_price

            order_items.append(
                {
                    "product": product,
                    "quantity": quantity,
                    "total_price": item_price,
                }
            )

        if total_price == 0:
            return Response(
                {"error": "결제할 상품이 없습니다."}, status=status.HTTP_400_BAD_REQUEST
            )

        order = Order.objects.create(
            user=request.user,
            total_price=total_price,
            buyer_name=request.user.username,
            merchant_uid=str(uuid.uuid4()),
        )

        for item in order_items:
            OrderItem.objects.create(
                order=order,
                product=item["product"],
                quantity=item["quantity"],
                total_price=item["total_price"],
            )

        token = get_port_one_token()

        prepare_url = "https://api.iamport.kr/payments/prepare"
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        prepare_data = {
            "merchant_uid": order.merchant_uid,
            "amount": float(total_price),
        }

        prepare_response = requests.post(
            prepare_url, json=prepare_data, headers=headers
        )
        prepare_result = prepare_response.json()

        if prepare_result.get("code") == 0:
            return Response(
                {
                    "merchant_uid": order.merchant_uid,
                    "amount": total_price,
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"error": prepare_result.get("message", "결제 준비 중 오류 발생")},
                status=status.HTTP_400_BAD_REQUEST,
            )


class KakaoPayCartApproveView(APIView):
    @transaction.atomic
    def post(self, request):
        imp_uid = request.data.get("imp_uid")
        merchant_uid = request.data.get("merchant_uid")

        if not imp_uid or not merchant_uid:
            return Response(
                {"error": "잘못된 결제 정보입니다."}, status=status.HTTP_400_BAD_REQUEST
            )

        order = get_object_or_404(Order, merchant_uid=merchant_uid)
        token = get_port_one_token()
        verify_url = f"https://api.iamport.kr/payments/{imp_uid}"
        headers = {"Authorization": f"Bearer {token}"}

        try:
            verify_response = requests.get(verify_url, headers=headers)
            verify_result = verify_response.json()

            if verify_result.get("code") != 0:
                return Response(
                    {
                        "error": verify_result.get(
                            "message", "결제 검증 중 오류가 발생했습니다."
                        )
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            payment_data = verify_result.get("response")
            if not payment_data:
                return Response(
                    {"error": "결제 정보가 유효하지 않습니다."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if payment_data["amount"] != order.total_price:
                return Response(
                    {"error": "결제 금액이 일치하지 않습니다."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if payment_data["status"] == "paid":
                order.is_paid = True
                order.imp_uid = imp_uid
                order.save()

                order_items = OrderItem.objects.filter(order=order)
                for item in order_items:
                    product = item.product

                    if product.stock < item.quantity:
                        raise ValueError(f"{product.name}의 재고가 부족합니다.")

                    product.stock -= item.quantity
                    product.save()

                CartItem.objects.filter(cart__user=request.user,
                                        product__in=[item.product for item in order_items]).delete()

                return Response(
                    {"message": "결제가 성공적으로 승인되었습니다."},
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"error": "결제가 완료되지 않았습니다."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        except ValueError as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_400_BAD_REQUEST
            )

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
