#!/usr/bin/python

import pika


def main():
	produce_message("Hello world!")


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
