from rest_framework import serializers
from .models import User, Status, Subscription, EventHistory


class UserSerializer(serializers.models):
    class Meta:
        model = User
        fields = '__all__'


class StatusSerializer(serializers.models):
    class Meta:
        model = Status
        fields = '__all__'


class SubscriptionSerializer(serializers.models):
    class Meta:
        model = Subscription
        fields = '__all__'


class EventHistorySerializer(serializers.models):
    class Meta:
        model = EventHistory
        fields = '__all__'
