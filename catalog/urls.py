from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import products, description

app_name = CatalogConfig.name

urlpatterns = [
    path('', products, name='products'),
    path('<int:pk>/catalog/', description, name='description'),
]
