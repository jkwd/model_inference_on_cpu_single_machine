import time
from common.utils import get_dataset, get_model, translate, sentiment
from common.constants import Experiment

def run(experiment: Experiment):
    full_start_time = time.time()
    
    # pipe for SENTIMENT, tokenizer + model for TRANSLATION
    pipe, tokenizer, model = get_model(experiment=experiment)
    texts = get_dataset(experiment=experiment)
    
    start_time = time.time()
    if experiment is Experiment.TRANSLATION:        
        outs = [translate(text, tokenizer, model) for text in texts]
    elif experiment is Experiment.SENTIMENT:
        outs = [sentiment(text, pipe) for text in texts]
    end_time = time.time()
    
    full_end_time = time.time()

    time_diff = end_time - start_time
    full_time_diff = full_end_time - full_start_time
    print(f"Model inference time taken: {time_diff}")
    print(f"Full time taken: {full_time_diff}")