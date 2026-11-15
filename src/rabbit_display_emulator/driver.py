import json

import aio_pika
from aio_pika.abc import AbstractIncomingMessage

from rabbit_display_emulator import Display


class Driver:

    EXCHANGE = 'message'
    EXCHANGE_TYPE = aio_pika.ExchangeType.TOPIC
    QUEUE = 'display'
    ROUTING_KEY = 'example.display'

    def __init__(self, initial_display: Display):
        self.display = initial_display or {}

    async def start(self, initial_display=None):
        self.connection = await aio_pika.connect_robust('amqp://guest:guest@localhost/')
        self.channel = await self.connection.channel()
        await self.channel.set_qos(prefetch_count=1)

        exchange = await self.channel.declare_exchange(self.EXCHANGE, self.EXCHANGE_TYPE)
        queue = await self.channel.declare_queue(self.QUEUE, durable=True)
        await queue.bind(exchange, routing_key=self.ROUTING_KEY)
        await queue.consume(self.on_message)

    async def stop(self):
        await self.connection.close()

    async def on_message(self, message: AbstractIncomingMessage):
        async with message.process():  # acks on success, rejects on exception
            print(f"   [x] Received: {message.body!r}")
            self.display.update(json.loads(message.body))
