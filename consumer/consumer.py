import pika as pk
from logging import warning


credentials = pk.PlainCredentials("ascan", "ascan")
connection = pk.BlockingConnection(
    pk.ConnectionParameters('rabbitmq', 5672, '/', credentials))
channel = connection.channel()

channel.queue_declare(queue='report')


def callback(ch, method, properties, body):
    warning(f"[x] Received {body}")


channel.basic_consume(
    queue="report", on_message_callback=callback, auto_ack=True)

warning('[*] waiting for messages. To exit press CTRL+C.')
channel.start_consuming()
