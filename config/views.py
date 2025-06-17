# mon_projet/views.py

from django.http import HttpResponse


def robots_txt(request):
    content = """
    User-agent: *
    Disallow: /admin/
    Disallow: /checkout/
    Disallow: /basket/
    Disallow: /account/
    Disallow: /password-reset/
    Disallow: /search/
    Allow: /
    """
    return HttpResponse(content.strip(), content_type="text/plain")
