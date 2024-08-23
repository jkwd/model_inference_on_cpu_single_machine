import time
from utils import get_model, get_dataset, get_num_cores
import ray

ctx = ray.init(
    ignore_reinit_error=True, 
    num_cpus=get_num_cores(),
)

@ray.remote
def predict(pipe, text):
    return pipe(text)[0]['label']

texts = get_dataset()
pipe = get_model()
pipe_id = ray.put(pipe)

start_time = time.time()
out_futures = [predict.remote(pipe_id, text) for text in texts]
out = ray.get(out_futures)
end_time = time.time()
time_diff = end_time - start_time

print(f"Time taken: {time_diff}")

ctx.shutdown()