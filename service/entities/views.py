from django.shortcuts import render
from django.db.models import Prefetch, F, Sum

from rest_framework.viewsets import ReadOnlyModelViewSet

from clients.models import Client
from entities.models import Subscription, Plan
from entities.serializers import SerializerSubscription, SerializerPlan


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = (Subscription.objects.select_related('plan')
                .prefetch_related
                (Prefetch('client', queryset=Client.objects.select_related('user')
                          .only('company_name', 'user__email')))
                ).annotate(price=F('service__full_price') -
                                 F('service__full_price') * F('plan__discount_percent') / 100.00)
    serializer_class = SerializerSubscription

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        response = super().list(request, *args, **kwargs)

        response_data = {'result': response.data}
        response_data['total_price'] = queryset.aggregate(total=Sum('price')).get('total')

        response.data = response_data

        return response


class PlanView(ReadOnlyModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = SerializerPlan
