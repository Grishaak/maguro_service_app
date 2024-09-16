from celery import shared_task


@shared_task
def set_price(subscription_id):
    from entities.models import Subscription

    subscription = Subscription.objects.get(id=subscription_id)
    new_price = subscription.service.full_price \
                - (subscription.service.full_price *
                   subscription.plan.disount_percent) / 100
    subscription.price = new_price
    subscription.save(save_model=False)
