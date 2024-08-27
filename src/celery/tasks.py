from celery import Celery
from common.utils import get_translation_model, translate, get_sentiment_model

app = Celery('tasks', 
             broker='redis://localhost:6379/0', 
             backend='redis://localhost:6379/0')


@app.task
def get_translation(text, tokenizer, model):
    tokenizer, model = get_translation_model()
    return translate(text, tokenizer, model)


@app.task
def get_sentiment(text):
    pipe = get_sentiment_model()
    return pipe(text)[0]['label']