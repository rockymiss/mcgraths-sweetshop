from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


def update_on_save(sender, instance, created, **kwargs):
    """
    Updates order total on lineitem 
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()
