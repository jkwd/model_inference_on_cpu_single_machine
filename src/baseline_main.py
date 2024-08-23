import time
from utils import get_model, get_dataset

texts = get_dataset()
pipe = get_model()

start_time = time.time()
outs = [pipe(text)[0]['label'] for text in texts]
end_time = time.time()
time_diff = end_time - start_time

print(f"Time taken: {time_diff}")