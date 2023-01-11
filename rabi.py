#!/usr/bin/env python
import pika

class Rabi():
    def __init__(self,q = None):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()

        print(self.connection)
        print(self.channel)
        self.q = "default" if q is None else q
        self._queue_declare(q=self.q)

    def _queue_declare(self,q):
        self.channel.queue_declare(queue=q)

    def push_to_q(self,context=""):
        # context is str
        self.channel.basic_publish(exchange='',
                            routing_key=self.q,
                            body=context)

    def listen_and_call(self,q=None,call=None):
        if q is None:
            q = self.q
        self.channel.basic_consume(queue=q, on_message_callback=call, auto_ack=True)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()

    def close(self):
        self.connection.close()      


    
