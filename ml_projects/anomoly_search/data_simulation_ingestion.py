from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

while True:
    data = {
        "timestamp": time.time(),
        "transaction_id": random.randint(1000, 9999),
        "amount": random.uniform(10, 1000),
        "account_id": random.randint(1, 100),
        "transaction_type": random.choice(["debit", "credit"])
    }
    producer.send('transaction_data', data)
    print(f"Sent: {data}")
    time.sleep(1)