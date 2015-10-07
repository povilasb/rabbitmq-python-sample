#!/usr/bin/python

from threading import Thread

import pika

import pika_utils


def main():
    consume_message()

def consume_message():
    connection = pika_utils.make_blocking_connection()
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

    consumer_tag = channel.basic_consume(on_msg_receive, queue = queue_name, no_ack = True)
    channel.start_consuming()

    channel.basic_cancel(consumer_tag)

    consumer_tag = channel.basic_consume(on_msg_receive, queue = queue_name, no_ack = True)
    channel.start_consuming()
    print "Finished consuming"

    while 1:
        pass

    connection.close()


def on_msg_receive(channel, method, properties, body):
    print("Received %r" % body)

    channel.stop_consuming()


if __name__ == "__main__":
    main()
