from django.db import models
from modelcluster.fields import ParentalKey

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import (FieldPanel, MultiFieldPanel,
                                  MultipleChooserPanel)
from wagtailvideos.edit_handlers import VideoChooserPanel


class HomePageGalleryImages(Orderable):
    """Between 1 and 5 images for the home page carousel."""

    page = ParentalKey("HomePage", related_name="gallery_images")

    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )  
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]


class HomePageSetoise(Orderable):
    page = ParentalKey("HomePage", related_name="gallery_setoise_part1")

    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]


class HomePageSetoise2(Orderable):
    page = ParentalKey("HomePage", related_name="gallery_setoise_part2")

    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]


class HomePageSetoise3(Orderable):
    page = ParentalKey("HomePage", related_name="gallery_setoise_part3")

    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]


class HomePage(Page):
    header_video = models.ForeignKey(
        'wagtailvideos.Video',
        related_name='+',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    content_panels = Page.content_panels + [
        VideoChooserPanel('header_video'),
    ]

    body = RichTextField(blank=True)

    contact_cta = models.CharField(
        blank=True, 
        verbose_name="Contact CTA",
        max_length=255,
        help_text="Contact forms CTA",
    )
    contact_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Contact CTA link",
        help_text="contact Page"
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("contact_cta"),
                FieldPanel("contact_cta_link"),
            ],
        ),
        FieldPanel('body'),
        MultipleChooserPanel(
            'gallery_images', 
            label="Gallery images", 
            chooser_field_name="image"
        ),
        MultipleChooserPanel(
            'gallery_setoise_part1', 
            label="Gallery images setoise", 
            chooser_field_name="image"
        ),
        MultipleChooserPanel(
            'gallery_setoise_part2', 
            label="Gallery images setoise 2", 
            chooser_field_name="image"
        ),
        MultipleChooserPanel(
            'gallery_setoise_part3', 
            label="Gallery images setoise 3", 
            chooser_field_name="image"
        )
    ]


