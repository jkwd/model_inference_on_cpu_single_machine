# import argparse
from spark_eval import spark_pandas_udf, spark_udf
from common.constants import Experiment

# parser=argparse.ArgumentParser(description="Spark Experiment")
# parser.add_argument('--run', '-r',  default='translation', nargs='?', choices=['translation', 'sentiment'])

# args=parser.parse_args()

# if args.run == 'translation':
#     experiment = Experiment('translation')
# elif args.run == 'sentiment':
#     experiment = Experiment('sentiment')

# spark_pandas_udf.run(experiment=experiment)

translation_time_diff_1, translation_full_time_diff_1 = spark_pandas_udf.run(experiment=Experiment('translation'))
sentiment_time_diff_1, sentiment_full_time_diff_1 = spark_pandas_udf.run(experiment=Experiment('sentiment'))

print(translation_time_diff_1, translation_full_time_diff_1)
print(sentiment_time_diff_1, sentiment_full_time_diff_1)

translation_time_diff_2, translation_full_time_diff_2 = spark_udf.run(experiment=Experiment('translation'))
sentiment_time_diff_2, sentiment_full_time_diff_2 = spark_udf.run(experiment=Experiment('sentiment'))

print(translation_time_diff_2, translation_full_time_diff_2)
print(sentiment_time_diff_2, sentiment_full_time_diff_2)