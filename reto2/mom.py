import pika, json
import mom_config

def get_files(file_type=None):
        connection = pika.BlockingConnection(pika.ConnectionParameters(mom_config.HOST, mom_config.PORT, '/', pika.PlainCredentials("user", "password")))
        channel = connection.channel()
        mensaje = file_type
        var = []
        def callback(channel, method, properties, body):
                var.append(json.loads(body))
        channel.stop_consuming()
        channel.basic_publish(exchange='file_listing', routing_key='request', body=mensaje)
        channel.basic_consume(queue="receive_files", on_message_callback=callback, auto_ack=True)
        channel.start_consuming()
        return var