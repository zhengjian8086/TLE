from django.urls import path, include
from .views import basic_search

urlpatterns = [
    path('search/', basic_search),
]
