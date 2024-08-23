from celery import Celery
from utils import get_model

app = Celery('tasks', 
             broker='redis://localhost:6379/0', 
             backend='redis://localhost:6379/0')

pipe = get_model()

@app.task
def get_sentiment(text):
    return pipe(text)[0]['label']