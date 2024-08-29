FROM apache/spark-py:latest

USER root

ENV PYSPARK_PYTHON=python3

WORKDIR ${SPARK_HOME}/app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt