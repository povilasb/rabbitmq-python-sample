#!/usr/bin/python

import pika


def main():
    for i in range(20):
        produce_message("Hello world!")

    raw_input("Hit ENTER to finish.")


def produce_message(msg):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters("localhost"))

    channel = connection.channel()
    channel.queue_declare(queue = "hello")
    channel.basic_publish(exchange = "", routing_key = "hello",
        body = msg)

    connection.close()


if __name__ == "__main__":
    main()
