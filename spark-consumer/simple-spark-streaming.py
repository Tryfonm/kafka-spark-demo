import findspark
findspark.init()
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("spark-streaming-console") \
    .getOrCreate()

kafka_brokers = "172.19.0.3:9092"
kafka_topic = "test-topic"

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_brokers) \
    .option("subscribe", kafka_topic) \
    .load()

query = df.selectExpr("CAST(value AS STRING)")\
    .writeStream.outputMode("append")\
    .format("console")\
    .start()

query.awaitTermination()
spark.stop()


