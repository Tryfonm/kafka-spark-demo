from kafka import KafkaConsumer

TOPIC_NAME = "test-topic"
BOOTSTRAP_SERVERS = "172.18.0.3:9092"


def main() -> None:
    consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=BOOTSTRAP_SERVERS)

    for message in consumer:
        print(message)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Server not found")
