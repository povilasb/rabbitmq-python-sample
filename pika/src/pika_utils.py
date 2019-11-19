import pika


def make_blocking_connection(host: str):
    credentials = pika.PlainCredentials('guest', 'guest')
    connection_params = pika.ConnectionParameters(
        host=host,
        credentials=credentials,
    )
    return pika.BlockingConnection(connection_params)
