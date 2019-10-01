import asyncio
import json

import aioamqp


async def main_async():
    _transport, protocol = await aioamqp.connect(
        host='172.17.0.2',
        on_error=on_error,
    )
    chann = await protocol.channel()

    await chann.basic_consume(on_msg, queue_name='tasks')


async def on_msg(chann, body, envelope, props):
    print('Received:', json.loads(body))
    print('  priority=', props.priority)
    await chann.basic_client_ack(delivery_tag=envelope.delivery_tag)


async def on_error(exception):
    print('RabbitMQ error:', exception)


def main():
    asyncio.get_event_loop().run_until_complete(main_async())


main()
