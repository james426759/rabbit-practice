#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('user', '5JX9hshZXp')
connection = pika.BlockingConnection(pika.ConnectionParameters('10.0.0.228', 5672, '/', credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')

message = ' '.join(sys.argv[1:]) or "Hello World!....."

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)

print(" [x] Sent 'Hello World!'")
connection.close()
