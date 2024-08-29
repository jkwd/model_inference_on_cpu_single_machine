import time
import pandas as pd
from common.utils import get_dataset, get_model, get_num_cores, predict
from common.constants import Experiment
from pyspark.sql import SparkSession

def run(experiment: Experiment):
    full_start_time = time.time()
    
    # Initialize a Spark session
    spark = SparkSession.builder.appName("SentimentAnalysis").getOrCreate()
    
    pipe, = get_model(experiment=experiment)

    # Define UDF    
    def spark_predict(text):
        return predict(input_text=text, pipe=pipe, experiment=experiment)
    udf_spark_predict = spark.udf.register("spark_predict", spark_predict)

    # Get data to spark df
    num_cores = get_num_cores()
    texts = get_dataset()
    df = spark.createDataFrame(pd.DataFrame(texts, columns=["texts"])).repartition(num_cores)

    # Cache to remove data loading to spark from timing as much as possible
    df.cache()

    # Get Sentiment via Pandas UDF
    # noop to force execution of UDF without writing to file
    start_time = time.time()
    result_df = df.withColumn("sentiment", udf_spark_predict(df["texts"]))
    result_df.write.format("noop").mode("overwrite").save()
    end_time = time.time()
    
    full_end_time = time.time()
    
    time_diff = end_time - start_time
    full_time_diff = full_end_time - full_start_time
    print(f"Model inference time taken: {time_diff}")
    print(f"Full time taken: {full_time_diff}")
    
    spark.stop()