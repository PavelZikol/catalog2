from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import products, description, main

app_name = CatalogConfig.name

urlpatterns = [
    path('', products, name='products'),
    path('main/', main, name='main'),
    path('<int:pk>/catalog/', description, name='description'),
]
