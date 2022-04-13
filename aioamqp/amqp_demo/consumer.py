import asyncio

import aioamqp


async def main():
    _transport, protocol = await aioamqp.connect(
        host='127.0.0.1',
        on_error=on_error,
    )
    chann = await protocol.channel()

    while True:
        await chann.basic_consume(on_msg, queue_name='tasks')


async def on_msg(chann, body, envelope, props):
    print('Received:', body)
    print('  priority=', props.priority)
    await chann.basic_client_ack(delivery_tag=envelope.delivery_tag)


async def on_error(exception):
    print('RabbitMQ error:', exception)


asyncio.run(main())
