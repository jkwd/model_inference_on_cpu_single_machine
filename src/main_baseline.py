import argparse
from baseline import run_baseline
from common.constants import Experiment

parser=argparse.ArgumentParser(description="Baseline Experiment")
parser.add_argument('--run', '-r',  default='translation', nargs='?', choices=['translation', 'sentiment'])

args=parser.parse_args()

if args.run == 'translation':
    experiment = Experiment('translation')
elif args.run == 'sentiment':
    experiment = Experiment('sentiment')

run_baseline.run(experiment=experiment)