from django.shortcuts import render
from django.db.models import Prefetch, F, Sum
from django.core.cache import cache
from django.conf import settings

from rest_framework.viewsets import ReadOnlyModelViewSet

from clients.models import Client
from entities.models import Subscription, Plan
from entities.serializers import SerializerSubscription, SerializerPlan


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = (Subscription.objects.select_related('plan')
                .prefetch_related
                (Prefetch('client', queryset=Client.objects.select_related('user')
                          .only('company_name', 'user__email')))
                )  #:.annotate(price=F('service__full_price') -
    #                  F('service__full_price') * F('plan__discount_percent') / 100.00)
    serializer_class = SerializerSubscription

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        response = super().list(request, *args, **kwargs)
        
        price_cache = cache.get(settings.PRICE_NAME)
        

        if price_cache:
            total_price = price_cache
        else:
            total_price = queryset.aggregate(total=Sum('price')).get('total')
            cache.set(settings.PRICE_NAME, total_price, 60**2)

        response_data = {'result': response.data}
        response_data['total_price'] = total_price
        response.data = response_data

        return response


class PlanView(ReadOnlyModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = SerializerPlan
