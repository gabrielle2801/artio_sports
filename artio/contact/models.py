from django.db import models
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.defaultfilters import pluralize
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
    landing_page_template = "contact/form_page_landing.html"
    page = ParentalKey('FormPage', on_delete=models.CASCADE, 
                       related_name='form_fields')


class FormPage(WagtailCaptchaEmailForm):
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
    
    def email_submission(instance, form):
        """ Send an email with the submission. """

        addresses = ['']
        content = ['Please see below submission\n', ]
        from_address = settings.EMAIL_HOST_USER
        subject = 'New Form Submission : %s' % instance.title

        # build up the email content
        for field, value in form.cleaned_data.items():
            if field in form.files:
                count = len(form.files.getlist(field))
                value = '{} file{}'.format(count, pluralize(count))
            elif isinstance(value, list):
                value = ', '.join(value)
            content.append('{}: {}'.format(field, value))
        content = '\n'.join(content)

        # create the email message
        email = EmailMessage(
            subject=subject,
            body=content,
            from_email=from_address,
            to=addresses
        )

        # attach any files submitted
        for field in form.files:
            for file in form.files.getlist(field):
                file.seek(0)
                email.attach(file.name, file.read(), file.content_type)

        # finally send the email
        email.send(fail_silently=True)
'''
--------------------------------------
class FormField(AbstractFormField):
    landing_page_template = "contact/form_page_landing.html"
    page = ParentalKey('FormPage', on_delete=models.CASCADE, 
                       related_name='form_fields')


class FormPage(WagtailCaptchaEmailForm):
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
--------------------------------------
 def email(self, form):
        text_content = render_to_string(
            '../contact/email_template.html',
            context={"form_fields"})

        html_content = render_to_string(
            "../contact/email_template.html",
            context={"form_fields"}
        )

        msg = EmailMultiAlternatives(
            "Subject here",
            text_content,
            'contact@artio-sports.com'
            ["gabrielleazadian@gmail.com"]
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()

def send_mail(self, form):
        # `self` is the FormPage, `form` is the form's POST data on submit

        # Email addresses are parsed from the FormPage's addresses field
        addresses = [x.strip() for x in self.to_address.split(',')]

        # Subject can be adjusted (adding submitted date), be sure to include the form's defined subject field
        submitted_date_str = date.today().strftime('%x')
        subject = f"{self.subject} - {submitted_date_str}"

        send_mail(subject, self.render_email(form),
                  addresses, self.from_address,)
    def get_data_fields(self):
        data_fields = [
            ('first_name'),
            ('last_name'),
            ('business_email'),
            ('phone_number'),
            ('job_title'),
            ('lets_us_a_message'),
        ]
        data_fields += super().get_data_fields()
        return data_fields
'''