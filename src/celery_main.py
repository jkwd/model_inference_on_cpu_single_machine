import time
from tasks import get_sentiment
from utils import get_dataset

# Get the dataset
texts = get_dataset()

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