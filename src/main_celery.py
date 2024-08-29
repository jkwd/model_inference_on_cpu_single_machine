# import argparse
from celery_eval import run_celery
from common.constants import Experiment

# parser=argparse.ArgumentParser(description="Baseline Experiment")
# parser.add_argument('--run', '-r',  default='translation', nargs='?', choices=['translation', 'sentiment'])

# args=parser.parse_args()

# if args.run == 'translation':
#     experiment = Experiment('translation')
# elif args.run == 'sentiment':
#     experiment = Experiment('sentiment')

# run_celery.run(experiment=experiment)

translation_time_diff, translation_full_time_diff = run_celery.run(experiment=Experiment('translation'))
sentiment_time_diff, sentiment_full_time_diff = run_celery.run(experiment=Experiment('sentiment'))

print(translation_time_diff, translation_full_time_diff)
print(sentiment_time_diff, sentiment_full_time_diff)