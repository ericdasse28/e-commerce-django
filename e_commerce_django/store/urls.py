from django.urls import path

from .views.home import Index, store

urlpatterns = [
    path("", Index.as_view(), name="homepage"),
    path("store", store, name="store"),
]
