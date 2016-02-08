import pika

def make_blocking_connection():
    """Create pika blocking connection with the specified parameters.

    Ars:
        config (object): options config parse from proxy.conf.
    """
    credentials = pika.PlainCredentials('user1', 'password1')
    connection_params = pika.ConnectionParameters(
        host = '192.168.1.240',
        credentials = credentials,
    )

    connection = pika.BlockingConnection(
        connection_params)

    return connection
