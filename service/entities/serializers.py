from rest_framework import serializers
from entities.models import Subscription, Plan


class SerializerPlan(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('__all__')


class SerializerSubscription(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.company_name')
    email = serializers.CharField(source='client.user.email')
    plan = SerializerPlan()
    price = serializers.SerializerMethodField('get_price')

    def get_price(self, instance: Subscription):
        pre_price = instance.service.full_price
        discount = pre_price * instance.plan.discount_percentage / 100
        return pre_price - discount

    class Meta:
        model = Subscription
        fields = ('pk', 'plan', 'client_name', 'email')
