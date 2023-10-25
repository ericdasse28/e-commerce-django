from django.http import HttpRequest
from django.shortcuts import redirect
from django.views import View
from loguru import logger
from store.models.customer import Customer
from store.models.order import Order
from store.models.product import Product


class CheckOut(View):
    def post(self, request: HttpRequest):
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        customer = request.session.get("customer")
        cart = request.session.get("cart")
        products = Product.get_products_by_id(list(cart.keys()))
        logger.info(f"{address} {phone} {customer} {cart} {products}")

        for product in products:
            logger.info(cart.get(str(product.id)))
            order = Order(
                customer=Customer(id=customer),
                product=product,
                price=product.price,
                address=address,
                phone=phone,
                quantity=cart.get(str(product.id)),
            )
            order.save()

        request.session["cart"] = {}

        return redirect("cart")
