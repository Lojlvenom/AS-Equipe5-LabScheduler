import pika

class Rabbit_Instance():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host= 'localhost'))
    channel = connection.channel()


    def create_queue(self, queue_name):
        self.channel.queue_declare(queue_name)
    
    def publish(self, routing_key, body):
        self.channel.basic_publish(exchange='',routing_key=routing_key, body=body)
    
    def consume(self, consume_queue, callback):
        self.channel.basic_consume(queue=consume_queue, on_message_callback=callback, auto_ack=True)
        self.channel.start_consuming()


rabbit_instance = Rabbit_Instance()

# notification_instance.create_queue('notification_queue')
# notification_instance.publish('notification_queue','alguma mensagem aleatoria')

# connection = pika.BlockingConnection(
#     pika.ConnectionParameters(host= 'localhost')
#     )
# channel = connection.channel()

# channel.queue_declare('notify_queue')