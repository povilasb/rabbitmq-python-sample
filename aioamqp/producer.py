import asyncio
import json
import sys

import aioamqp


async def main_async(msg_priority: int):
    _transport, protocol = await aioamqp.connect(
        host='127.0.0.1',
        on_error=on_error,
    )
    chann = await protocol.channel()
    await chann.queue_declare('tasks', arguments={'x-max-priority': 3})
    msg = {
        'name': 'task1',
        'priority': msg_priority,
    }
    await chann.publish(json.dumps(msg), '', 'tasks',
                        properties={'priority': msg_priority})


async def on_error(exception):
    print('RabbitMQ error:', exception)


def main():
    msg_priority = int(sys.argv[1]) if len(sys.argv) >= 2 else 1
    asyncio.get_event_loop().run_until_complete(main_async(msg_priority))


main()
