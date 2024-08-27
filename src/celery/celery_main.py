import time
from tasks import get_translation, get_sentiment
from common.utils import get_translation_dataset, get_sentiment_dataset

def run_translation():
    texts = get_translation_dataset()

    # Start the timer
    start_time = time.time()

    # Dispatch tasks to Celery workers
    task_results = [get_translation.delay(text) for text in texts]

    # Collect the results
    labels = [task.get() for task in task_results]

    # End the timer
    end_time = time.time()
    time_diff = end_time - start_time

    print(f"Time taken: {time_diff}")

def run_sentiment():
    texts = get_sentiment_dataset()

    # Start the timer
    start_time = time.time()

    # Dispatch tasks to Celery workers
    task_results = [get_sentiment.delay(text) for text in texts]

    # Collect the results
    labels = [task.get() for task in task_results]

    # End the timer
    end_time = time.time()
    time_diff = end_time - start_time

    print(f"Time taken: {time_diff}")