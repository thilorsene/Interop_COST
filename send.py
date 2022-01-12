#!/usr/bin/env python
import pika
import json
from datetime import datetime

def send_command_rbmq(order):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port='5672'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')
   
    

    channel.basic_publish(exchange='', routing_key='hello', body=json.dumps(order))
    print(" [x] Sent 'Hello World!'")
    connection.close()
