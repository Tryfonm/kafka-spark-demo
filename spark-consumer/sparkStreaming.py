import findspark
findspark.init()
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder \
    .appName("KafkaConsumer") \
    .getOrCreate()

# Define Kafka parameters
kafka_brokers = "172.19.0.3:9092"  # Replace with your Kafka broker(s) address
kafka_topic = "test-topic"  # Replace with your Kafka topic name

# Read messages from Kafka topic using structured streaming
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_brokers) \
    .option("subscribe", kafka_topic) \
    .load()

# Set the query to process the Kafka messages
query = df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")\
    .writeStream.outputMode("append")\
    .format("console")\
    .start()

# Wait for the streaming query to terminate
query.awaitTermination()

# Stop the SparkSession when done
spark.stop()

