from django.urls import path
from artio.products.views import ArtioCatalogueView, JoutesCatalogueView

urlpatterns = [
    path("e_catalogue/", ArtioCatalogueView.as_view(), name='e_catalogue'),
    path("joute_catalogue/", JoutesCatalogueView.as_view(), name='j_catalogue'),
]