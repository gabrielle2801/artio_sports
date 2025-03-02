<<<<<<< HEAD
from django.db import models
=======
>>>>>>> 3a2d8aa8c1b0f4975ce54c17064465ab66e104bd

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index


# Create your models here.
class MentionIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]
<<<<<<< HEAD


=======
>>>>>>> 3a2d8aa8c1b0f4975ce54c17064465ab66e104bd
