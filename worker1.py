#!/usr/bin/env python
import pika
import time

credentials = pika.PlainCredentials('user', '5JX9hshZXp')
connection = pika.BlockingConnection(pika.ConnectionParameters('10.0.0.228', 5672, '/', credentials))

channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

print( ' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print("[x] Received %r" % (body,))
    time.sleep(body.decode("utf-8").count("."))
    print( " [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume('task_queue', callback)

channel.start_consuming()
