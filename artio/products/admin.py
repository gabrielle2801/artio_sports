from django.contrib import admin
from artio.products.models import Product, ProductCustomField, ProductArtio

admin.site.register(Product)
admin.site.register(ProductCustomField)
admin.site.register(ProductArtio)
