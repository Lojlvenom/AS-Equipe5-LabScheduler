# -*- coding: utf-8 -*-
import pika
import json
import smtplib
import sys
sys.path.append('../server')
from rabbit_server import rabbit_instance as rb




def callback(ch,method,propreties,body):
    content = json.loads(body)
    send_email(content=content)
    print("este e o conteudo da mensagem =   {} ".format(body))
   

def send_email(content):
    reciver_list = []
    sender = "notificationServiceProjetoASW@gmail.com"
    password = "notification@@@@"
    subject = "Detalhe de reserva"
    for email in content['email_list']:
        receiver = email
        print(receiver)
        datetime = content['date_time']
        spaces = content['spaces']
        obs = content['obs']
        body = "Detalhes da reserva - Local: {} - Data/hora: {} - OBS:{}".format(spaces,datetime,obs)
        # header
       # header
        message = f"""From:{sender}
        To: {receiver}
        Subject: {subject}\n
        {body}
        """
        email_server = smtplib.SMTP("smtp.gmail.com", 587)
        email_server.starttls()
        try:
            email_server.login(sender,password)
            print("Logged in...")
            email_server.sendmail(sender, receiver, message)
            print("Email has been sent!")

        except smtplib.SMTPAuthenticationError:
            print("unable to sign in")

rb.consume(consume_queue='notification_queue', callback= callback)



