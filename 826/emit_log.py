#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('user', 'Fu148fL4qg')
connection = pika.BlockingConnection(pika.ConnectionParameters('10.0.0.228', 5672, '/', credentials))

channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print( " [x] Sent %r" % (message,))
connection.close()
