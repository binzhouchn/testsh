#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.100.129.81'))
channel = connection.channel()
#创建exchange的名称为logs，指定类型为fanout
channel.exchange_declare(exchange='logs', exchange_type='fanout')
#删除随机创建的消息队列
result = channel.queue_declare(queue='task_queue')
queue_name = 'task_queue'
channel.queue_bind(exchange='logs', queue=queue_name)
print(' [*] Waiting for logs. To exit press CTRL+C')
def callback(ch, method, properties, body):
    print(" [x] %r" % body)
channel.basic_consume(queue_name, callback)
channel.start_consuming()