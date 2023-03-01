import pika, json

def get_files():
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials("user", "password")))
        channel = connection.channel()
        mensaje = 'list'
        var = []
        def callback(channel, method, properties, body):
                var.append(json.loads(body))
        channel.stop_consuming()
        channel.basic_publish(exchange='file_listing', routing_key='request', body=mensaje)
        channel.basic_consume(queue="receive_files", on_message_callback=callback, auto_ack=True)
        channel.start_consuming()
        return var