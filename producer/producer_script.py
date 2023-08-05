from kafka import KafkaProducer

TOPIC_NAME = "test-topic"
BOOTSTRAP_SERVERS = "172.18.0.3:9092"


def main() -> None:
    producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS)

    msg = input("Enter message: ").encode("utf-8")

    while True:
        try:
            msg = input("Enter message: ").encode("utf-8")
            producer.send(TOPIC_NAME, msg)
            producer.flush()
        except KeyboardInterrupt:
            print("\n\nStopping producer...\n")
            break


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Server not found")
