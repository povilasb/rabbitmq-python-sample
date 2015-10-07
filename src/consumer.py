#!/usr/bin/python

from threading import Thread
import time

import pika

import pika_utils


def main():
    connection = pika_utils.make_blocking_connection()
    channel = connection.channel()
    t = Thread(target=consume_message, args=(channel,))
    t.start()

    time.sleep(2)
    print "Stopping consuming"
    channel.stop_consuming()

    print "Joining thread"
    t.join()
    print "Thread joined"

    channel.close()
    connection.close()

def consume_message(channel):
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

    print "Start consuming"
    channel.start_consuming()
    print "Finished consuming"


def on_msg_receive(channel, method, properties, body):
    print("Received %r" % body)


if __name__ == "__main__":
    main()
