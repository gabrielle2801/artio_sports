from django.contrib.sitemaps import Sitemap
from oscar.apps.catalogue.models import Product, Category
from wagtail.models import Page
from django.contrib.sites.models import Site
from urllib.parse import urljoin

# Sitemap pour les produits
class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Product.objects.filter(is_public=True)

    def lastmod(self, obj):
        return obj.date_updated
      
    def location(self, obj):
        url = obj.get_absolute_url()
        # Vérifie si URL est absolue (commence par http)
        if url.startswith('http'):
            return url
        # Sinon, ajoute domaine complet
        current_site = Site.objects.get_current()
        return urljoin(f"https://{current_site.domain}", url)


# Sitemap pour les catégories
class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Category.objects.all()
    
    def location(self, obj):
        url = obj.get_absolute_url()
        if url.startswith('http'):
            return url
        current_site = Site.objects.get_current()
        return urljoin(f"https://{current_site.domain}", url)


# Sitemap pour les pages Wagtail
class PageSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Page.objects.live().public()
    
    def location(self, obj):
        # Essaye d'utiliser full_url si disponible
        if hasattr(obj, 'full_url') and obj.full_url:
            return obj.full_url
        # Sinon, construit proprement l'URL absolue
        current_site = Site.objects.get_current()
        url = obj.url
        if not url.startswith('/'):
            url = '/' + url
        return urljoin(f"https://{current_site.domain}", url)
