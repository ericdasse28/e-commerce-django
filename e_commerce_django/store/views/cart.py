from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from loguru import logger

from e_commerce_django.store.models.product import Product


class Cart(View):
    def get(self, request: HttpRequest):
        ids = list(request.session.get("cart").keys())
        products = Product.get_products_by_id(ids)
        logger.info(products)

        return render(request, "store/cart.html", {"products": products})
