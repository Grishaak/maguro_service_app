from django.db.models.signals import post_delete
from django.dispatch import receiver

from django.core.cache import cache
from django.conf import settings


@receiver(post_delete, sender=None)
def by_deleting_subscription(*args, **kwargs):
        cache.delete(settings.PRICE_NAME)
