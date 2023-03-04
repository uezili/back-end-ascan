import pika
import json


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port='5672'))
channel = connection.channel()

message = {
    'event_type': 'SUBSCRIPTION_PURCHASED',
    'data': {
        'user_id': 1
    }
}

channel.basic_publish(
    exchange='', routing_key='subscriptions', body=json.dumps(message))
print("deu bom")

connection.close()
