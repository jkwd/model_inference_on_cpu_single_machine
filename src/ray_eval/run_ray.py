import time
from common.utils import get_num_cores, get_model, get_dataset, predict
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
    def ray_predict(input_text, pipe):
        return predict(input_text=input_text, pipe=pipe, experiment=experiment)
    
    pipe = get_model(experiment=experiment)
    pipe_id = ray.put(pipe)
    texts = get_dataset(experiment=experiment)
    
    start_time = time.time()
    outs = ray.get([ray_predict.remote(text, pipe_id) for text in texts])
    end_time = time.time()
    
    full_end_time = time.time()

    time_diff = end_time - start_time
    full_time_diff = full_end_time - full_start_time
    print(f"Model inference time taken: {time_diff}")
    print(f"Full time taken: {full_time_diff}")
    
    ray.shutdown()