import time
from common.utils import get_num_cores, get_translation_dataset, get_translation_model, translate, get_sentiment_model, get_sentiment_dataset
import ray

def run_translation():
    full_start_time = time.time()
    num_cpus = get_num_cores()
    ctx = ray.init(
        num_cpus=num_cpus,
        ignore_reinit_error=True,
    )

    @ray.remote
    def ray_translate(input_text, tokenizer, model):
        return translate(input_text, tokenizer, model)
    
    texts = get_translation_dataset()
    tokenizer, model = get_translation_model()
    tokenizer_id = ray.put(tokenizer)
    model_id = ray.put(model)

    start_time = time.time()
    outs = ray.get([ray_translate.remote(text, tokenizer_id, model_id) for text in texts])
    end_time = time.time()

    full_end_time = time.time()

    time_diff = end_time - start_time
    full_time_diff = full_end_time - full_start_time
    print(f"Translation time taken: {time_diff}")
    print(f"Full time taken: {full_time_diff}")
    
def run_sentiment():
    full_start_time = time.time()
    num_cpus = get_num_cores()
    ctx = ray.init(
        num_cpus=num_cpus,
        ignore_reinit_error=True,
    )

    @ray.remote
    def ray_sentiment(input_text, pipe):
        return pipe(input_text)[0]['label']
    
    texts = get_sentiment_dataset()
    pipe = get_sentiment_model()
    pipe_id = ray.put(pipe)

    start_time = time.time()
    outs = ray.get([ray_sentiment.remote(text, pipe_id) for text in texts])
    end_time = time.time()

    full_end_time = time.time()

    time_diff = end_time - start_time
    full_time_diff = full_end_time - full_start_time
    print(f"Translation time taken: {time_diff}")
    print(f"Full time taken: {full_time_diff}")