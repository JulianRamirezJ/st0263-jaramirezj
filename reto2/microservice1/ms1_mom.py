import pika
import json
import time
import os
import ms1_config

def list_files(file_type=None):
    file_list = []
    for archivo in os.listdir(ms1_config.DIR):
        if file_type is None or archivo.endswith(file_type):
            file_list.append(archivo)
    return file_list

def send_response(channel, files):
    response_json = json.dumps(files)
    print(response_json)
    channel.basic_publish(exchange='file_listing', routing_key='receive', body=response_json)
    print("[x] Enviada respuesta al programa RabbitMQ %r")

def receive_message(channel):
    channel.basic_consume(queue='request_files', on_message_callback=callback, auto_ack=True)
    print("[*] Esperando mensajes...")
    channel.start_consuming()

def callback(ch, method, properties, body):
    str_body = body.decode('utf-8')
    if body is not None:
        files = list_files(str_body)
    else:
        files = list_files()
    send_response(channel, files)
    channel.stop_consuming()

def connect_with_retry(host, port, credentials, virtual_host='/', max_retries=10, retry_delay=5):
    parameters = pika.ConnectionParameters(host=host, port=port, virtual_host=virtual_host, credentials=credentials)
    retries = 0
    while retries < max_retries:
        try:
            connection = pika.BlockingConnection(parameters)
            return connection
        except pika.exceptions.AMQPConnectionError as e:
            time.sleep(retry_delay)
            retries += 1
    raise e   

while True:
    #connection = pika.BlockingConnection(pika.ConnectionParameters(ms1_config.HOST, ms1_config.PORT, '/', pika.PlainCredentials("user", "password")))
    credentials = pika.PlainCredentials('user', 'password')
    connection = connect_with_retry(ms1_config.HOST, ms1_config.PORT, credentials)
    channel = connection.channel()
    receive_message(channel)