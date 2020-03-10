#!/usr/bin/env python
import pika

class Question:

    def __init__(self, _id, question, score=None):
        self.id = _id
        self.question = question
        self.score = score


    def to_string(self):
        result = "Question(id:{}, question:{}, score:{})".format(self.id, self.question, self.score)
        return result

qq = Question(15,'没钱怎么办',2)



connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='10.100.129.81'))
channel = connection.channel()

channel.queue_declare(queue='hello')

# channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
channel.basic_publish(exchange='', routing_key='hello', body=qq.to_string())
print(" [x] Sent 'Hello World!'")
connection.close()