# from celeryapp import app
from src.common.utils import get_model, predict
from src.common.constants import Experiment
from celery import Celery
import os

broker = os.getenv('CELERY_BROKER', 'redis://localhost:6379/0')
backend = os.getenv('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')

app = Celery('tasks', 
             broker=broker, 
             backend=backend)

app.conf.update(
    task_serializer='json',
    result_serializer='json',
    accept_content=['json'],
)

@app.task
def celery_predict(text:str, exp_data:dict):
    experiment = Experiment.from_dict(exp_data)
    pipe = get_model(experiment=experiment)
    return predict(input_text=text, pipe=pipe, experiment=experiment)