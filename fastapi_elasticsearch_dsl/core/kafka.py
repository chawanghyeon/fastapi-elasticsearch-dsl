from kafka import KafkaConsumer

class KafkaConsumerClient:
    def __init__(self, broker_url: str, topic: str):
        self.consumer = KafkaConsumer(topic, bootstrap_servers=[broker_url])

    def consume_messages(self):
        for message in self.consumer:
            # ...existing code...
            print(f"Received message: {message.value}")
