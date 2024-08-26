import time
import pandas as pd
from utils import get_dataset, get_model, get_num_cores
from pyspark.sql import SparkSession
from pyspark.sql.functions import pandas_udf
from pyspark.sql.types import StringType


# Initialize a Spark session
spark = SparkSession.builder.appName("SentimentAnalysis").getOrCreate()

# Define UDF
# https://docs.databricks.com/en/machine-learning/train-model/huggingface/model-inference-nlp.html
@pandas_udf('string')
def sentiment_udf(texts: pd.Series) -> pd.Series:
    pipe = get_model()
    sentiments = [out['label'] for out in pipe(texts.to_list(), batch_size=1)]
    return pd.Series(sentiments)

def analyze_sentiment(text):
    pipe = get_model()
    return pipe(text)[0]["label"]
udf_analyze_sentiment = spark.udf.register("analyze_sentiment", analyze_sentiment)

# Get data to spark df
num_cores = get_num_cores()
texts = get_dataset()
df = spark.createDataFrame(pd.DataFrame(texts, columns=["texts"])).repartition(num_cores)

# Cache to remove data loading to spark from timing as much as possible
df.cache()

# Get Sentiment via UDF
# noop to force execution of UDF without writing to file
start_time = time.time()
sentiment_df = df.withColumn("sentiment", udf_analyze_sentiment(df["texts"]))
sentiment_df.write.format("noop").mode("overwrite").save()
end_time = time.time()
time_diff = end_time - start_time
print(f"Time taken for UDF: {time_diff}")


# Get Sentiment via Pandas UDF
# noop to force execution of UDF without writing to file
start_time = time.time()
sentiment_df_2 = df.withColumn("sentiment", sentiment_udf(df.texts).alias('translation'))
sentiment_df_2.write.format("noop").mode("overwrite").save()
end_time = time.time()
time_diff = end_time - start_time
print(f"Time taken for Pandas UDF: {time_diff}")