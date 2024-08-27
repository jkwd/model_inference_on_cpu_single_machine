import time
from common.utils import get_translation_dataset, get_translation_model, translate, get_sentiment_model, get_sentiment_dataset

def run_translate():
    full_start_time = time.time()

    texts = get_translation_dataset()
    tokenizer, model = get_translation_model()

    start_time = time.time()
    outs = [translate(text, tokenizer, model) for text in texts]
    end_time = time.time()

    full_end_time = time.time()

    time_diff = end_time - start_time
    full_time_diff = full_end_time - full_start_time
    print(f"Translation time taken: {time_diff}")
    print(f"Full time taken: {full_time_diff}")
    
def run_sentiment():
    full_start_time = time.time()

    texts = get_sentiment_dataset()
    pipe = get_sentiment_model()

    start_time = time.time()
    outs = [pipe(text)[0]['label'] for text in texts]
    end_time = time.time()

    full_end_time = time.time()

    time_diff = end_time - start_time
    full_time_diff = full_end_time - full_start_time
    print(f"Translation time taken: {time_diff}")
    print(f"Full time taken: {full_time_diff}")