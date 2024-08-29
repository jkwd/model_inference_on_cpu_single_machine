import argparse
from spark import spark_pandas_udf
from common.constants import Experiment

parser=argparse.ArgumentParser(description="Spark Experiment")
parser.add_argument('--run', '-r',  default='translation', nargs='?', choices=['translation', 'sentiment'])

args=parser.parse_args()

if args.run == 'translation':
    experiment = Experiment('translation')
elif args.run == 'sentiment':
    experiment = Experiment('sentiment')

spark_pandas_udf.run(experiment=experiment)