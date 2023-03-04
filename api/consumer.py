import json
import pika as pk


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
