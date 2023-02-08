from rest_framework import serializers
from .models import User, Status, Subscription, EventHistory


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class EventHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventHistory
        fields = '__all__'
