import pika
import time
from databases import Database
from db_operations import updateSqliteTable
import json

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port='5672'))
channel = connection.channel()

channel.queue_declare(queue='hello', durable=False)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % json.loads(body.decode()))
    time.sleep(body.count(b'.'))
    result = json.loads(body.decode())
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)
    updateSqliteTable(result)
    


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='hello', on_message_callback=callback)

channel.start_consuming()

#---------------------
