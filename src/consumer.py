#!/usr/bin/python

import pika


def main():
	consume_message()


def consume_message():
	connection = pika.BlockingConnection(
		pika.ConnectionParameters("localhost"))

	channel = connection.channel()
	channel.queue_declare(queue = "hello")
	channel.basic_consume(on_msg_receive, queue = "hello", no_ack = True)
	channel.start_consuming()

	connection.close()


def on_msg_receive(channel, method, properties, body):
	print("Received %r" % body)


if __name__ == "__main__":
	main()
