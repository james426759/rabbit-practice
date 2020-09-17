#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('user', 'Fu148fL4qg')
connection = pika.BlockingConnection(pika.ConnectionParameters('10.0.0.228', 5672, '/', credentials))

channel = connection.channel()

channel.queue_declare(queue='hello')

print( ' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print( " [x] Received %r" % (body.decode("utf-8"),))

channel.basic_consume('hello', callback)

channel.start_consuming()
