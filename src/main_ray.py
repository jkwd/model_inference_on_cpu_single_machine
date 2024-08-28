import argparse
from ray_eval import run_ray
from common.constants import Experiment

parser=argparse.ArgumentParser(description="Ray Experiment")
parser.add_argument('--run', '-r',  default='translation', nargs='?', choices=['translation', 'sentiment'])

args=parser.parse_args()

if args.run == 'translation':
    experiment = Experiment('translation')
elif args.run == 'sentiment':
    experiment = Experiment('sentiment')

run_ray.run(experiment=experiment)