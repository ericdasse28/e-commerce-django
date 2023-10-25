from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from loguru import logger
from store.models.order import Order


class OrderView(View):
    def get(self, request: HttpRequest):
        customer = request.session.get("customer")
        orders = Order.get_orders_by_customer(customer)
        logger.info(orders)

        return render(request, "store/orders.html", {"orders": orders})
