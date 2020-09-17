#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('user', '5JX9hshZXp')
connection = pika.BlockingConnection(pika.ConnectionParameters('10.0.0.228', 5672, '/', credentials))

channel = connection.channel()

channel.queue_delete(queue='hello')
