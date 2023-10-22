from django.urls import path

from e_commerce_django import store
from e_commerce_django.store.views.home import Index

urlpatterns = [
    path("/", Index.as_view(), name="homepage"),
    path("store", store, name="store"),
]
