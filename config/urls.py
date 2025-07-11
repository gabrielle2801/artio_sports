from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from django.apps import apps
from .views import robots_txt
from artio.search import views as search_views
from sitemaps import (
    ProductSitemap,
    CategorySitemap,
    PageSitemap,
    WagtailPageSitemap,
)
from django.contrib.sitemaps.views import sitemap
# from django.views.decorators.cache import cache_page
from oscar.core.loading import get_model


Product = get_model('catalogue', 'Product')

product_info = {
    'queryset': Product.objects.filter(is_public=True, structure='standalone', 
                                       stockrecords__num_in_stock__gt=0),
    'date_field': 'date_updated',
}
sitemaps = {
    'products': ProductSitemap,
    'categories': CategorySitemap,
    'pages': PageSitemap,
    'wagtail_pages': WagtailPageSitemap(),
}

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("search/", search_views.search, name="search"),
    path("robots.txt", robots_txt),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('boutique/', include(apps.get_app_config('oscar').urls[0])),
    path("__reload__/", include("django_browser_reload.urls")),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include('artio.standardpages.urls')),
    path("", include('artio.products.urls')),
    path("", include(wagtail_urls)),
    
    
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
