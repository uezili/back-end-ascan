import pika
from logging import warning


def callback(ch, method, properties, body):
    warning(" [x] Received %r" % body)

credentials = pika.PlainCredentials("ascan", "ascan")
connection = pika.BlockingConnection(
    pika.ConnectionParameters('rabbitmq', 5672, '/', credentials))
channel = connection.channel()

channel.queue_declare(queue='event_history', durable=True)

channel.basic_consume(
    queue='event_history', on_message_callback=callback, auto_ack=True)

warning(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
