# search_filter/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.search_restaurants, name='search_restaurants'),
]
