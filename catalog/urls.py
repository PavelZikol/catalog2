from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import products, description, main, main_3

app_name = CatalogConfig.name

urlpatterns = [
    path('', products, name='product'),
    path('main/', main, name='main'),
    path('main/', main_3, name='main_3'),
    path('<int:pk>/catalog/', description, name='description'),
]
