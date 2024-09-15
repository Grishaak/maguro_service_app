from rest_framework import serializers
from entities.models import Subscription, Plan



class SerializerPlan(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields =  ('__all__')

class SerializerSubscription(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.company_name')
    email = serializers.CharField(source='client.user.email')
    plan = SerializerPlan()
    class Meta:
        model = Subscription
        fields = ('pk', 'plan', 'client_name', 'email')
