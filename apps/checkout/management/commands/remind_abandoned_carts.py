from django.core.management.base import BaseCommand
from oscar.core.loading import get_model
from django.utils.timezone import now, timedelta
from apps.checkout.emails import send_abandoned_cart_email

Basket = get_model('basket', 'Basket')


class Command(BaseCommand):
    help = 'Relance les paniers abandonnés depuis 24h'

    def handle(self, *args, **options):
        cutoff = now() - timedelta(hours=24)
        baskets = Basket.objects.filter(status='Open', date_created__lt=cutoff)

        for basket in baskets:
            # ⛔ Évite de relancer un panier déjà relancé
            if getattr(basket, 'meta', {}).get('relance_envoyee'):
                continue

            if not basket.owner or not basket.owner.email:
                continue

            email = basket.owner.email
            name = basket.owner.get_full_name() or "Client"
            cart_url = "http://127.0.0.1:8000/boutique/basket/"
            cart_summary = ", ".join([
                f"{line.quantity}× {line.product.get_title()}"
                for line in basket.lines.all()
            ])

            # ✅ Envoi de l'email
            send_abandoned_cart_email(email, name, cart_url, cart_summary)

            # ✅ Marquer ce panier comme "relancé"
            basket.meta['relance_envoyee'] = True
            basket.save()

            self.stdout.write(self.style.SUCCESS(f"Email envoyé à {email}"))
