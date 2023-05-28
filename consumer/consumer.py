import pika
from logging import warning


credentials = pika.PlainCredentials("ascan", "ascan")
connection = pika.BlockingConnection(
    pika.ConnectionParameters('rabbitmq', 5672, '/', credentials))
channel = connection.channel()

channel.queue_declare(queue='event_history')


def callback(ch, method, properties, body):
    warning(f" [x] Received  {body}")


channel.basic_consume(
    'event_history', callback, auto_ack=True)

warning(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
