import json
import pika as pk

# from django.core.exceptions import ObjectDoesNotExist
# from .models import Subscription, EventHistory, Status, User


class SubscriptionProcessor:
    def __init__(self):
        self._connection = pk.BlockingConnection(
            pk.ConnectionParameters(host='rabbitmq', port='5672'))
        self._channel = self._connection.channel()
        self._channel.queue_declare(queue='subscriptions')

    def start_consuming(self):
        self._channel.basic_consume(
            queue='subscriptions', on_message_callback=self._on_message, auto_ack=True)
        self._channel.start_consuming()

    def _on_message(self, channel, method, properties, body):
        message = json.loads(body)
        event_type = message['event_type']
        data = message['data']
        print(event_type, data)

# class SubscriptionProcessor2:
#    def __init__(self):
#        self._host = "rabbitmq"
#        self._port = "5672"

#    def start(self):
#        connection2 = pk.BlockingConnection(
#            pk.ConnectionParameters(host=self._host, port=self._port)
#        )
#        channel = connection2.channel()
#        channel.queue_declare("subscriptions")

#        def _callback(self, ch, method, properties, body):
#            print(body)
#        channel.basic_consume(queue="subscriptions",
#                              on_message_callback=_callback, auto_ack=True)
#        print('[*] Waiting for messages. To exit press CTRL + C.')
#        channel.start_consuming()
