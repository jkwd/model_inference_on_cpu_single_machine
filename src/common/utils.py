import typing
import pandas as pd
from transformers import pipeline, T5Tokenizer, T5ForConditionalGeneration, Pipeline
from .constants import SENTIMENT_MODEL, SENTIMENT_DATA, TRANSLATION_DATA, TRANSLATION_MODEL, Experiment

### MODEL ###
def get_sentiment_model() -> Pipeline:
    # device=-1 for CPU
    pipe = pipeline("sentiment-analysis", 
                    model=SENTIMENT_MODEL, 
                    tokenizer=SENTIMENT_MODEL, 
                    max_length=512, 
                    truncation=True,
                    device=-1)
    return pipe

def get_translation_model() -> Pipeline:
    tokenizer = T5Tokenizer.from_pretrained(TRANSLATION_MODEL)
    model = T5ForConditionalGeneration.from_pretrained(TRANSLATION_MODEL)
    model.config.max_new_tokens = 1000
    
    pipe = pipeline('translation_en_to_fr', model=model, tokenizer=tokenizer, device=-1)
    return pipe

def get_model(experiment: Experiment) -> Pipeline:
    if experiment is Experiment.TRANSLATION:
        return get_translation_model()
    elif experiment is Experiment.SENTIMENT:
        return get_sentiment_model()

### MODEL ###


### DATASET ###
def get_sentiment_dataset() -> typing.List[str]:
    df = pd.read_csv(SENTIMENT_DATA)
    df = df.dropna(subset=['text'])
    return list(df['text'].values)[:5]

def get_translation_dataset() -> typing.List[str]:
    df = pd.read_json(TRANSLATION_DATA, lines=True)
    df = df.dropna(subset=['quote'])
    return list(df['quote'].values)[:5]

def get_dataset(experiment: Experiment) -> typing.List[str]:
    if experiment is Experiment.TRANSLATION:
        return get_translation_dataset()
    elif experiment is Experiment.SENTIMENT:
        return get_sentiment_dataset()

### DATASET ###

### INFERENCE ###
def translate(input_text:str, pipe: Pipeline) -> str:
    # input_text = "translate English to French: " + input_text
    # input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    # outputs = model.generate(input_ids, max_new_tokens=1000)
    # result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    # return result
    return pipe(input_text)[0]['translation_text']

def sentiment(input_text:str, pipe: Pipeline) -> str:
    return pipe(input_text)[0]['label']

def predict(input_text:str, pipe: Pipeline, experiment: Experiment):
    if experiment is Experiment.TRANSLATION:
        return translate(input_text=input_text, pipe=pipe)
    elif experiment is Experiment.SENTIMENT:
        return sentiment(input_text=input_text, pipe=pipe)

### INFERENCE ###

def get_num_cores() -> int:
    return 2