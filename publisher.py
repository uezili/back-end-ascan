import pika
import json


credentials = pika.PlainCredentials("ascan", "ascan")
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost', 5672, '/', credentials))
channel = connection.channel()


SUBSCRIPTION_PURCHASED = {
  "event_type": "SUBSCRIPTION_PURCHASED",
  "data": {
    "user_id": 123
  }
}

SUBSCRIPTION_CANCELED = {
  "event_type": "SUBSCRIPTION_CANCELED",
  "data": {
    "subscription_id": 456
  }
}

SUBSCRIPTION_RESTARTED = {
  "event_type": "SUBSCRIPTION_RESTARTED",
  "data": {
    "subscription_id": 789
  }
}

channel.exchange_declare(exchange='event_history', exchange_type='fanout')
channel.queue_bind(exchange='event_history', queue='event_history')
#channel.basic_publish(exchange='event_history', routing_key="", body=JsonResponse(body))

channel.basic_publish(exchange='event_history', routing_key="", body=json.dumps(message))
print(f" [x] Sent {message}")
connection.close()
