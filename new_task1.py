#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('user', '5JX9hshZXp')
connection = pika.BlockingConnection(pika.ConnectionParameters('10.0.0.228', 5672, '/', credentials))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!....."

channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
channel.basic_qos(prefetch_count=1)
print( " [x] Sent %r" % (message,))
connection.close()
