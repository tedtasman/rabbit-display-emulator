import json
import random
import time
from dataclasses import asdict

import pika
from rabbit_display_emulator.display import Display, Shared, Side

EXCHANGE = 'message'
QUEUE = 'display'
ROUTING_KEY = 'example.display'

display = Display(
    left=Side(
        text="ABC",
        large=f"{random.randint(0,999):03d}",
        small=f"{random.randint(0,99):02d}",
        pips=random.randint(0,3)
    ),
    right=Side(
        text="XYZ",
        large=f"{random.randint(0,999):03d}",
        small=f"{random.randint(0,99):02d}",
        pips=random.randint(0,3)
    ),
    shared=Shared(
        time=f"{random.randint(0,12):02d}:{random.randint(0,59):02d}",
        small=f"{random.randint(0,99):02d}",
    )
)


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange=EXCHANGE, exchange_type='topic')
channel.queue_declare(queue=QUEUE, durable=True)
channel.queue_bind(queue=QUEUE, exchange=EXCHANGE, routing_key=ROUTING_KEY)

try:
    while True:
        display = Display(
            left=Side(
                text=f"{chr(random.randint(65,90))}{chr(random.randint(65,90))}{chr(random.randint(65,90))}",
                large=f"{random.randint(0,999):03d}",
                small=f"{random.randint(0,99):02d}",
                pips=random.randint(0,3)
            ),
            right=Side(
                text=f"{chr(random.randint(65,90))}{chr(random.randint(65,90))}{chr(random.randint(65,90))}",
                large=f"{random.randint(0,999):03d}",
                small=f"{random.randint(0,99):02d}",
                pips=random.randint(0,3)
            ),
            shared=Shared(
                time=f"{random.randint(0,12):02d}:{random.randint(0,59):02d}",
                small=f"{random.randint(0,99):02d}",
            )
        )
        channel.basic_publish(
            exchange=EXCHANGE,
            routing_key=ROUTING_KEY,
            body=json.dumps(asdict(display)),
            properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent),
        )
        print(" [x] Sent update")
        time.sleep(1)
        
except KeyboardInterrupt:
    connection.close()