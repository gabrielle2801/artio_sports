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

    mention_cta = models.CharField(
        blank=True, 
        verbose_name="Mention CTA",
        max_length=255,
        help_text="Mention CTA",
    )
    mention_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="mention CTA link",
        help_text="mention Page"
    )
    policy_cta = models.CharField(
        blank=True, 
        verbose_name="Mention CTA",
        max_length=255,
        help_text="Mention CTA",
    )
    policy_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="policy CTA link",
        help_text="policy Page"
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("contact_cta"),
                FieldPanel("contact_cta_link"),
                FieldPanel("mention_cta"),
                FieldPanel("mention_cta_link"),
                FieldPanel("policy_cta"),
                FieldPanel("policy_cta_link"),
            ],
        ),
        FieldPanel('body'),
    ]


