from django.http import JsonResponse
from rest_framework import viewsets
from .models import Subscription, User, Status, SendMessage
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializer import SubscriptionSerializer, UserSerializer, StatusSerializer
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
            return Response({"error": "Field body is none."}, status=status.HTTP_400_BAD_REQUEST)
        
        credentials = pika.PlainCredentials("ascan", "ascan")
        connection = pika.BlockingConnection(
            pika.ConnectionParameters('rabbitmq', 5672, '/', credentials))
        channel = connection.channel()

        # channel.exchange_declare(exchange='event_history', exchange_type='direct')
        channel.exchange_declare(exchange='event_history', exchange_type='fanout')

        channel.queue_bind(exchange='event_history', queue='event_history')

        channel.basic_publish(exchange='event_history', routing_key="", body=json.dumps(body))

        connection.close()
        print(body)
        return Response({"success": "Message sent successfully."}, status=status.HTTP_201_CREATED)

        