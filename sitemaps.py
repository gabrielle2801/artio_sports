from django.contrib.sitemaps import Sitemap
from oscar.apps.catalogue.models import Product, Category
from wagtail.models import Page
from django.contrib.sites.models import Site


# Sitemap pour les produits
class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Product.objects.filter(is_public=True)

    def lastmod(self, obj):
        return obj.date_updated
      
    def location(self, obj):
        return obj.get_absolute_url()


# Sitemap pour les catégories
class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Category.objects.all()
    
    def location(self, obj):
        return obj.get_absolute_url()


# Sitemap pour les pages Wagtail
class PageSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Page.objects.live().public()
    
    def location(self, obj):
        current_site = Site.objects.get_current()
        return f"https://{current_site.domain}{obj.url}"
