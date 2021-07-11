import pika
import json

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host= 'localhost')
    )
channel = connection.channel()


def callback(ch,method,propreties,body):
    print("este e o conteudo da mensagem =   {} ".format(body))

channel.basic_consume(queue='notify_queue', on_message_callback= callback, auto_ack=True)
channel.start_consuming()