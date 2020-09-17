#!/usr/bin/env python
import pika
import time

credentials = pika.PlainCredentials('user', '5JX9hshZXp')
connection = pika.BlockingConnection(pika.ConnectionParameters('10.0.0.228', 5672, '/', credentials))

channel = connection.channel()

channel.queue_declare(queue='hello')

print( ' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print("[x] Received %r" % (body,))
    time.sleep(body.decode("utf-8").count("."))
    print( " [x] Done")
    #ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_consume('hello', callback)

channel.start_consuming()
