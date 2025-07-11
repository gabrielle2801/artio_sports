# checkout/emails.py

from django.conf import settings
from sib_api_v3_sdk.configuration import Configuration
from sib_api_v3_sdk.api_client import ApiClient
from sib_api_v3_sdk.api.transactional_emails_api import TransactionalEmailsApi
from sib_api_v3_sdk.models import SendSmtpEmail


def send_abandoned_cart_email(to_email, customer_name, cart_url, cart_summary):
    configuration = Configuration()
    configuration.api_key['api-key'] = settings.BREVO_API_KEY

    with ApiClient(configuration) as api_client:
        api_instance = TransactionalEmailsApi(api_client)
        email = SendSmtpEmail(
            to=[{"email": to_email}],
            template_id=settings.BREVO_TEMPLATE_ID_ABANDONED_CART,
            params={
                "CUSTOMER_NAME": customer_name,
                "CART_URL": cart_url,
                "CART_SUMMARY": cart_summary
            }
        )
        api_instance.send_transac_email(email)
