# some_app/views.py
from django.views.generic import TemplateView


class MentionView(TemplateView):
    template_name = "standardpages/mention_page.html"


class PolicyView(TemplateView):
    template_name = 'standardpages/policy_page.html'


class TermsConditionView(TemplateView):
    template_name = 'standardpages/terms_condition_sale.html'




