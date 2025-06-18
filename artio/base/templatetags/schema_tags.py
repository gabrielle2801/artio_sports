from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag(takes_context=True)
def render_product_schema(context, product):
    request = context['request']
    return render_to_string("catalogue/includes/schema_product.json", {
        'product': product,
        'request': request,
    })
