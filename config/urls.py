from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
<<<<<<< HEAD

from artio.search import views as search_views
# from artio.standardpages.views import MentionView, PolicyView

urlpatterns = [
=======
from django.apps import apps
from artio.search import views as search_views

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
>>>>>>> 3a2d8aa8c1b0f4975ce54c17064465ab66e104bd
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("search/", search_views.search, name="search"),
<<<<<<< HEAD
=======
    path('boutique/', include(apps.get_app_config('oscar').urls[0])),
>>>>>>> 3a2d8aa8c1b0f4975ce54c17064465ab66e104bd
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
<<<<<<< HEAD
=======
    path("", include('artio.products.urls')),
>>>>>>> 3a2d8aa8c1b0f4975ce54c17064465ab66e104bd
    path("", include(wagtail_urls)),
    
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
