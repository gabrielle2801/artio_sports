# some_app/views.py
from django.views.generic import TemplateView


class MentionView(TemplateView):
    template_name = "standardpages/mention_page.html"


class PolicyView(TemplateView):
    template_name = 'standardpages/policy_page.html'
<<<<<<< HEAD
=======


class TermsConditionView(TemplateView):
    template_name = 'standardpages/terms_condition_sale.html'




>>>>>>> 3a2d8aa8c1b0f4975ce54c17064465ab66e104bd
