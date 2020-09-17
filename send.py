#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('user', 'Fu148fL4qg')
connection = pika.BlockingConnection(pika.ConnectionParameters('10.0.0.228', 5672, '/', credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
