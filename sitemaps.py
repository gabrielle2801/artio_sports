from django.contrib.sitemaps import Sitemap
from oscar.apps.catalogue.models import Product, Category
from wagtail.models import Page


class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Product.objects.filter(is_public=True)

    def lastmod(self, obj):
        return obj.date_updated

    def location(self, obj):
        # On retourne seulement le chemin relatif, pas l'URL complète
        return obj.get_absolute_url()


class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Category.objects.all()

    def location(self, obj):
        # Retourne seulement le chemin relatif, sans domaine ni protocole
        return obj.get_absolute_url()


class PageSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Page.objects.live().public()

    def location(self, obj):
        # obj.url_path est un chemin relatif commençant par '/'
        return obj.url_path

