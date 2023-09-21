FROM openjdk:11.0.11-jre-slim-buster

RUN apt update -y && apt upgrade -y 
RUN apt install -y curl wget nano iproute2 iputils-ping software-properties-common ssh net-tools ca-certificates screen
RUN apt install -y python3 python3-pip && update-alternatives --install "/usr/bin/python" "python" "$(which python3)" 1

ENV SPARK_VERSION=3.0.2 \
    HADOOP_VERSION=3.2 \
    SPARK_HOME=/opt/spark \
    PATH="SPARK_HOME:${PATH}"

RUN wget --no-verbose -O apache-spark.tgz "https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" \
    && mkdir -p /opt/spark \
    && tar -xf apache-spark.tgz -C /opt/spark --strip-components=1 \
    && rm apache-spark.tgz

EXPOSE 8080 7077
ENV PYSPARK_SUBMIT_ARGS='--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.2,org.apache.kafka:kafka_2.13:3.5.0 pyspark-shell'
WORKDIR /opt/spark/workspace

RUN pip3 install findspark
COPY simple-spark-streaming.py /opt/spark/workspace/simple-spark-streaming.py

ENTRYPOINT ["python3", "/opt/spark/workspace/simple-spark-streaming.py"]
