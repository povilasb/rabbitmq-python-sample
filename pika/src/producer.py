#!/usr/bin/python

import pika
import pika_utils


def main():
    #for i in range(20):
    produce_message('Hello world!')


def produce_message(msg):
    connection = pika_utils.make_blocking_connection('127.0.0.1')

    channel = connection.channel()
    channel.queue_declare(queue='tasks', durable=True)
    channel.basic_publish(exchange='', routing_key='tasks', body=msg)

    connection.close()


if __name__ == '__main__':
    main()
