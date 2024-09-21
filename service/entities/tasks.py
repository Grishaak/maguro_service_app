from celery import shared_task
from django.db.models import F
from time import sleep
from celery_singleton import Singleton
from django.conf import settings
from django.core.cache import cache


@shared_task(base=Singleton)
def set_price(subscription_id):
    from entities.models import Subscription
    
    sleep(3)

    subscription = Subscription.objects.filter(id=subscription_id).annotate(
            annotated_price=F('service__full_price')
            - F('service__full_price')
            * F('plan__discount_percent') / 100.00).first()

    cache.delete(settings.PRICE_NAME)
    subscription.price = subscription.annotated_price
    subscription.save()
