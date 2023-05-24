import pika
from logging import warning


credentials = pika.PlainCredentials("ascan", "ascan")
connection = pika.BlockingConnection(
    pika.ConnectionParameters('rabbitmq', 5672, '/', credentials))
channel = connection.channel()

channel.queue_declare(queue='report')


def callback(ch, method, properties, body):
    warning(f"[x] Received {body}")


channel.basic_consume(
    queue="report", on_message_callback=callback, auto_ack=True)

warning('[*] waiting for messages. To exit press CTRL+C.')
