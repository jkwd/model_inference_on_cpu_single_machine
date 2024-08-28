import time
from src.celery_eval.tasks import celery_predict
from common.utils import get_dataset, get_model
from common.constants import Experiment

def run(experiment:Experiment):
    full_start_time = time.time()
    
    texts = get_dataset(experiment=experiment)
    pipe = get_model(experiment=experiment) # To predownload model to cache
    
    start_time = time.time()
    # Dispatch tasks to Celery workers
    task_results = [celery_predict.delay(text, experiment.to_dict()) for text in texts]

    # Collect the results
    outs = [task.get() for task in task_results]
    end_time = time.time()
    
    full_end_time = time.time()

    time_diff = end_time - start_time
    full_time_diff = full_end_time - full_start_time
    print(f"Model inference time taken: {time_diff}")
    print(f"Full time taken: {full_time_diff}")
    print(outs)