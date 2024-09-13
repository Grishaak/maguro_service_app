from django.shortcuts import render
from django.db.models import Prefetch

from rest_framework.viewsets import ReadOnlyModelViewSet

from clients.models import Client
from entities.models import Subscription, Plan
from entities.serializers import SerializerSubscription


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all().prefetch_related(
        Prefetch('client',
            queryset=Client.objects.select_related('user').only('company_name', 'user__email')),
        Prefetch('plan',
            queryset=Plan.objects.only('plan_type')))
    serializer_class = SerializerSubscription
