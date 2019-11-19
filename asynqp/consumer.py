import asyncio

import asynqp


async def main_async(loop) -> None:
    stop_consuming = asyncio.Future()
    # To stop consuming we would need to
    # stop_consuming.set_result(None)

    conn = await asynqp.connect('127.0.0.1', 5672, username='guest',
                                password='guest')
    chann = await conn.open_channel()
    queue = await chann.declare_queue('tasks')
    await queue.consume(
        lambda msg: loop.create_task(handle_msg(msg))
    )

    # Block the event loop until somebody fulfills stop_consuming future
    await stop_consuming


async def handle_msg(msg: asynqp.Message) -> None:
    # See https://asynqp.readthedocs.io/en/v0.4/reference.html#message-objects
    print('Received:', msg.body)
    msg.ack()


def main() -> None:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_async(loop))


main()
