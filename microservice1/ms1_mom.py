import pika, json
import os

def list_files():
    file_list = []
    for archivo in os.listdir('/home/ubuntu/st0263-231/rabbitmq-python/files'):
        file_list.append(archivo)
    return file_list

def send_response(channel, files):
    response_json = json.dumps(files)
    print(response_json)
    channel.basic_publish(exchange = 'file_listing', routing_key = 'receive', body = response_json)
    print("[x] Enviada respuesta al programa RabbitMQ %r")

def receive_message(channel):
    channel.basic_consume(queue = 'request_files', on_message_callback = callback, auto_ack = True)
    print("[*] Esperando mensajes...")
    channel.start_consuming()

def callback(ch, method, properties, body):
    files = list_files()
    send_response(channel, files)
    channel.stop_consuming()

while True:
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials("user", "password")))
    channel = connection.channel()
    receive_message(channel)