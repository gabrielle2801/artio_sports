from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel
from django.core.paginator import Paginator
from django.template.response import TemplateResponse


class Product(Page):
    template = 'products/product.html'

    def get_context(self, request):
        context = super().get_context(request)

        context['products'] = Product.objects.child_of(self).live()[:6]

        return context 
        
    sku = models.CharField(max_length=255)
    short_description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('sku'),
        FieldPanel('price'),
        FieldPanel('image'),
        FieldPanel('short_description'),
        InlinePanel('custom_fields', label='Custom fields'),
    ]


class ProductPage(Page):
    template = 'products/product_page.html'

    def get_context(self, request):
        context = super().get_context(request)

        context['products'] = Product.objects.child_of(self).live()[:6]

        return context 


class ProductCustomField(Orderable):
    product = ParentalKey(Product, on_delete=models.CASCADE,  
                          related_name='custom_fields')
    name = models.CharField(max_length=255)
    options = models.CharField(max_length=500, null=True, blank=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('options')
    ]

    def shop(request):
        products = Product.objects.live()
        p = Paginator(products, 10)
        # shows number of items in page
        totalProducts = (p.count)
        pageNum = request.GET.get('page', 1)
        page1 = p.page(pageNum)

        return TemplateResponse(request, 'products/product.html', {
            'products': totalProducts,
            'dataSaved': page1
        })


class ProductArtio(models.Model):
    name = models.CharField(max_length=100, blank=True)
    version = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    pdf = models.FileField(upload_to='pdf', blank=True, null=True)
    img = models.ImageField(upload_to='catalogue_sete/', blank=True, null=True)

    def __str__(self):
        return self.name