from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from entities.models import Subscription
from entities.serializers import SerializerSubscription


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SerializerSubscription
