from django.contrib.sitemaps import Sitemap
# from oscar.core.loading import get_model
from oscar.apps.catalogue.models import Product, Category
from wagtail.models import Page
from django.utils.text import slugify


# Product = get_model('catalogue', 'Product')


class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        '''
        Ne récupère que les produits "parents", 
        pas les variantes (tailles, couleurs)
        '''
        return Product.objects.filter(is_public=True, parent__isnull=True)

    def location(self, obj):
        # Récupère l’URL initiale
        url = obj.get_absolute_url()

        # Sépare le slug si nécessaire
        parts = url.strip("/").split("/")
        if len(parts) >= 3:
            # Exemple : /boutique/catalogue/t-shirt-bleu-xl_55/
            cleaned_slug = slugify(parts[-1].split("_")[0])
            cleaned_url = "/".join(parts[:-1] + [cleaned_slug])
        else:
            cleaned_url = slugify(url)

        return "/" + cleaned_url + "/"


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
        # Pages classiques non-Wagtail si applicable
        return []

    def location(self, obj):
        return obj.get_absolute_url()
    

class WagtailPageSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Page.objects.live().public().specific().exclude(slug="home")

    def location(self, page):
        url = page.url
        if url:  # évite les None
            return url
        return ""


