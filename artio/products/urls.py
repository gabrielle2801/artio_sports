from django.urls import path
from artio.products.views import ArtioCatalogueView

urlpatterns = [
    path("e_catalogue/", ArtioCatalogueView.as_view(), name='e_catalogue'),
]