from rest_framework import serializers
from entities.models import Subscription

class SerializerSubscription(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.company_name')
    email = serializers.CharField(source='client.user.email')

    class Meta:
        model = Subscription
        fields = ('pk', 'plan_id','client_name', 'email')

