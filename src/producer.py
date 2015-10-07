#!/usr/bin/python

import pika
import pika_utils


def main():
	for i in range(20):
		produce_message("Hello world!")

	raw_input("Hit ENTER to finish.")


def produce_message(msg):
	connection = pika_utils.make_blocking_connection()

	channel = connection.channel()
	channel.basic_publish(exchange = "my_msgs", routing_key = "consumer1",
		body = msg)

	connection.close()


if __name__ == "__main__":
	main()
