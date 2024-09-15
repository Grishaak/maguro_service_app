from django.shortcuts import render
from django.db.models import Prefetch

from rest_framework.viewsets import ReadOnlyModelViewSet

from clients.models import Client
from entities.models import Subscription, Plan
from entities.serializers import SerializerSubscription, SerializerPlan


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = (Subscription.objects.select_related('plan')
                .prefetch_related
                (Prefetch('client', queryset=Client.objects.select_related('user')
                          .only('company_name', 'user__email'))))
    serializer_class = SerializerSubscription


class PlanView(ReadOnlyModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = SerializerPlan
