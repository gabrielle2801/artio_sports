from django.urls import path
<<<<<<< HEAD
from artio.standardpages.views import MentionView, PolicyView
=======
from artio.standardpages.views import (MentionView, PolicyView,
                                       TermsConditionView)

>>>>>>> 3a2d8aa8c1b0f4975ce54c17064465ab66e104bd

urlpatterns = [
    path("mentions_legales/", MentionView.as_view(), name='mention_legales'),
    path("politique_de_confidentialite/", PolicyView.as_view(), 
         name='policy_page'),
<<<<<<< HEAD
=======
    path("cgv/", TermsConditionView.as_view(), name='terms_condition_sale'), 
>>>>>>> 3a2d8aa8c1b0f4975ce54c17064465ab66e104bd
]