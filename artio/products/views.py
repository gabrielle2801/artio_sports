from django.views.generic import ListView
from artio.products.models import ProductArtio

# Create your views here.


class ArtioCatalogueView(ListView):
    model = ProductArtio
    template_name = 'products/e_catalogue.html'
    context_object_name = 'artio_catalog'