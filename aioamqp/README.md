Publish and consume messages over RabbitMQ.

## Prerequisites

1. RabbitMQ running

```bash
$ docker run -d rabbitmq:3-management
```

2. Python 3.5+

## Running the samples

```bash
$ pip install -r requirements.txt
$ python3 producer.py 1  # publishes msg with priority 1
$ python3 producer.py 2  # publishes msg with priority 2
$ python3 producer.py 1  # publishes msg with priority 1
$ python3 consumer.py  # tasks with higher priority number are received first
Received: {'name': 'task1', 'priority': 2}
Received: {'name': 'task1', 'priority': 1}
Received: {'name': 'task1', 'priority': 1}
```
