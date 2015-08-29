#!/usr/bin/python

import pika


def main():
    consume_message()


def consume_message():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters("192.168.1.222"))

    channel = connection.channel()

    channel.exchange_declare(
        exchange = 'my_msgs',
        type = 'direct'
    )

    listen_queue = channel.queue_declare(exclusive=True)
    queue_name = listen_queue.method.queue

    channel.queue_bind(
        exchange = 'my_msgs',
        queue = queue_name,
        routing_key = "consumer1"
    )

    channel.basic_consume(on_msg_receive, queue = queue_name, no_ack = True)
    channel.start_consuming()

    connection.close()


def on_msg_receive(channel, method, properties, body):
    print("Received %r" % body)


if __name__ == "__main__":
    main()
