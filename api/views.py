from django.http import JsonResponse
from rest_framework import viewsets
from .models import Subscription, User, Status
from .serializer import SubscriptionSerializer, UserSerializer, StatusSerializer
import pika


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


def send_message(request):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq', port='5672'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_publish(
        exchange='', routing_key='hello', body='Hello World!')
    print(" [x] Sent 'Hello World!'")

    connection.close()

    return JsonResponse({'message': 'Message sent to RabbitMQ'})
