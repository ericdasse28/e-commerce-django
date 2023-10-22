from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from loguru import logger
from store.models.category import Category
from store.models.product import Product


class Index(View):
    """Index view class."""

    def post(self, request: HttpRequest):
        product = request.POST.get("product")
        remove = request.POST.get("remove")
        cart = request.session.get("cart")

        if cart:
            quantity = cart.get(product)

            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session["cart"] = cart
        logger.info(f"Cart: {request.session['cart']}")

        return redirect("homepage")

    def get(self, request):
        return HttpResponseRedirect(f"/store{request.get_full_path()[1:]}")


def store(request: HttpRequest):
    cart = request.session.get("cart")
    if not cart:
        request.session["cart"] = {}

    products = {}
    categories = Category.get_all_categories()
    category_id = request.GET.get("category")
    if category_id:
        products = Product.get_all_products_by_category_id(category_id)
    else:
        products = Product.get_all_products()

    data = {}
    data["products"] = products
    data["categories"] = categories

    logger.info(f"You are {request.session.get('email')}")
    return render(request, "store/index.html", data)
