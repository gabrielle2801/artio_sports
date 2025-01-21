from django.urls import path
from artio.standardpages.views import MentionView, PolicyView

urlpatterns = [
    path("mentions_legales/", MentionView.as_view(), name='mention_legales'),
    path("politique_de_confidentialite/", PolicyView.as_view(), 
         name='policy_page'),
]