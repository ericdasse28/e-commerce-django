from django.urls import path

from .middlewares.auth import auth_middleware
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.home import Index, store
from .views.login import Login, logout
from .views.orders import OrderView
from .views.signup import SignUp

urlpatterns = [
    path("", Index.as_view(), name="homepage"),
    path("store", store, name="store"),
    path("signup", SignUp.as_view(), name="signup"),
    path("login", Login.as_view(), name="login"),
    path("logout", logout, name="logout"),
    path("cart", auth_middleware(Cart.as_view()), name="cart"),
    path("checkout", CheckOut.as_view(), name="checkout"),
    path("orders", auth_middleware(OrderView.as_view()), name="orders"),
]
