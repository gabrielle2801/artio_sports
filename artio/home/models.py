from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtailvideos.edit_handlers import VideoChooserPanel


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
    ]