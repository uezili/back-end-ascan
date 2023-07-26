from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .models import EventHistory, User, Subscription, Status
from .serializer import SubscriptionSerializer, UserSerializer, StatusSerializer

from django.http import Http404

import pika
import json


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class SendMessageView(APIView):
    
    def post(self, request):

        body = request.data

        if not body:
            return Response({"error": "Field body is none."}, status=HTTP_400_BAD_REQUEST)
        
        event_type = str(request.data.get('event_type'))
        data = request.data.get('data')

        if event_type == 'SUBSCRIPTION_PURCHASED':
            self._process_subscription_purchased(data)
        elif event_type == 'SUBSCRIPTION_CANCELED':
            self._process_subscription_canceled(data)
        elif event_type == 'SUBSCRIPTION_RESTARTED':
            self._process_subscription_restarted(data)
        else:
            return Response({'error': 'Unknown event.'}, status=HTTP_400_BAD_REQUEST)
        
        credentials = pika.PlainCredentials("ascan", "ascan")
        connection = pika.BlockingConnection(
            pika.ConnectionParameters('rabbitmq', 5672, '/', credentials))
        channel = connection.channel()

        channel.exchange_declare(exchange='event_history', exchange_type='fanout')

        channel.queue_bind(exchange='event_history', queue='event_history')

        channel.basic_publish(exchange='event_history', routing_key="", body=json.dumps(body))

        connection.close()
        
        return Response({"success": "Message sent successfully."}, status=HTTP_201_CREATED)

    def _process_subscription_purchased(self, data):
        try:
            user_id = data['user_id']
            status_name = 'active'

            user = User.objects.get(id=data['user_id'])
            status = Status.objects.get(name=status_name)

            subscription = Subscription.objects.create(user_id=user, status_id=status)
            EventHistory.objects.create(subscription_id=subscription, type='SUBSCRIPTION_PURCHASED')
            return Response({"success": "Register successfully."}, status=HTTP_201_CREATED)

        except User.DoesNotExist:
            raise Http404(f"User not found: {user_id}")

    def _process_subscription_canceled(self, data):
        try:
            status_name = "canceled"
            subscription = Subscription.objects.get(id=data['subscription_id'])
            subscription.status_id = Status.objects.get(name=status_name)
            subscription.save()

            EventHistory.objects.create(subscription_id=subscription, type='SUBSCRIPTION_CANCELED')
        
        except Subscription.DoesNotExist:
            raise Http404(f"Subscription not found: {data['subscription_id']}")

    def _process_subscription_restarted(self, data):
        try:
            subscription = Subscription.objects.get(id=data['subscription_id'])
            subscription.status_id = Status.objects.get(name='active')
            subscription.save()

            EventHistory.objects.create(subscription_id=subscription, type='SUBSCRIPTION_RESTARTED')
        
        except Subscription.DoesNotExist:
            raise Http404(f"Subscription not found: {data['subscription_id']}")
