from django.db import models
from django import forms

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

from modelcluster.fields import ParentalKey


class JoutesEventPage(Page):
    
    # Introduction simple
    intro = RichTextField(blank=True)
    header_title = models.CharField(
        max_length=150,
        blank=True,
        help_text="Titre personnalisé à afficher dans le header"
)
    # Contenu principal flexible
    content = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title", help_text="Titre de section")),
        ('paragraph', blocks.RichTextBlock(features=["h2", "h3", "bold", "italic", "link"], help_text="Texte enrichi")),
        ('image', ImageChooserBlock(help_text="Image illustrative")),
    ], use_json_field=True, blank=True)

    # Vidéo externe
    video_url = models.URLField(blank=True, help_text="URL de la vidéo (YouTube embed, Vimeo, etc.)")

    # Bloc FAQ SEO
    faq = StreamField([
        ('question', blocks.StructBlock([
            ('question_text', blocks.CharBlock(required=True, help_text="Texte de la question")),
            ('answer_text', blocks.RichTextBlock(required=True, help_text="Texte de la réponse")),
        ]))
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('header_title'),
        FieldPanel('content'),
        FieldPanel('video_url'),
        FieldPanel('faq'),
        InlinePanel('event_product_links', label="Produits liés"),
    ]

    class Meta:
        verbose_name = "Page Événement - Joutes Sétoises"


# Modèle de liaison PRODUITS sans FK MySQL
class JoutesEventPageProduct(models.Model):
    page = ParentalKey(
        JoutesEventPage,
        on_delete=models.CASCADE,
        related_name='event_product_links'
    )

    # On stocke l'ID du produit Oscar sous forme d'Integer (ou CharField si tu utilises des UUID dans Oscar)
    product_id = models.PositiveIntegerField(
        help_text="ID du produit Oscar",
        null=True,
        blank=True
    )

    panels = [
        FieldPanel('product_id'),
    ]

    class Meta:
        verbose_name = "Produit lié à un événement"
        verbose_name_plural = "Produits liés aux événements"
