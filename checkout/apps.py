from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        """
        When a line item is saved or deleted the custom update total
        method will be called to update totals automatically
        """
        import checkout.signals
