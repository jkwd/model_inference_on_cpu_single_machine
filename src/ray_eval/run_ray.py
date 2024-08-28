import time
from common.utils import get_num_cores, get_model, get_dataset, translate, sentiment
from common.constants import Experiment
import ray

def run(experiment: Experiment):
    full_start_time = time.time()
    num_cpus = get_num_cores()
    ctx = ray.init(
        num_cpus=num_cpus,
        ignore_reinit_error=True,
    )
    
    @ray.remote
    def ray_translate(input_text, tokenizer, model):
        return translate(input_text, tokenizer, model)
    
    @ray.remote
    def ray_sentiment(input_text, pipe):
        return sentiment(input_text=input_text, pipe=pipe)
    
    # pipe for SENTIMENT, tokenizer + model for TRANSLATION
    pipe, tokenizer, model = get_model(experiment=experiment)
    if experiment is Experiment.TRANSLATION:
        tokenizer_id = ray.put(tokenizer)
        model_id = ray.put(model)
    elif experiment is Experiment.SENTIMENT:
        pipe_id = ray.put(pipe)
    texts = get_dataset(experiment=experiment)
    
    start_time = time.time()
    if experiment is Experiment.TRANSLATION:
        outs = ray.get([ray_translate.remote(text, tokenizer_id, model_id) for text in texts])
    elif experiment is Experiment.SENTIMENT:
        outs = ray.get([ray_sentiment.remote(text, pipe_id) for text in texts])
    end_time = time.time()
    
    full_end_time = time.time()

    time_diff = end_time - start_time
    full_time_diff = full_end_time - full_start_time
    print(f"Model inference time taken: {time_diff}")
    print(f"Full time taken: {full_time_diff}")
    
    ray.shutdown()