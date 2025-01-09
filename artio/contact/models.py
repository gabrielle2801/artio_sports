from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtailcaptcha.models import WagtailCaptchaEmailForm
from wagtail.fields import RichTextField
from django.utils.functional import cached_property
from wagtail.admin.panels import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
)


class FormField(AbstractFormField):
    
    page = ParentalKey('FormPage', on_delete=models.CASCADE, 
                       related_name='form_fields')


class FormPage(WagtailCaptchaEmailForm):
    template = "contact/form_page.html"
    landing_page_template = "contact/form_page_landing.html"
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel("intro"),
        InlinePanel("form_fields", label="Form fields"),
        FieldPanel("thank_you_text", classname="full"),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("from_address", classname="col6"),
                        FieldPanel("to_address", classname="uv pip col6"),
                    ]
                ),
                FieldPanel("subject"),
            ],
            "Email Notification Config",
        ),
    ]

    @cached_property
    def contact_page(self):
        return self.get_parent().specific

    def get_context(self, request, *args, **kwargs):
        context = super(FormPage, self).get_context(request, *args, **kwargs)
        context["contact_page"] = self.contact_page
        return context
    
    