import typing
import pandas as pd
from transformers import pipeline, T5Tokenizer, T5ForConditionalGeneration
from .constants import SENTIMENT_MODEL, SENTIMENT_DATA, TRANSLATION_DATA, TRANSLATION_MODEL, Experiment


def get_sentiment_model() -> pipeline:
    # device=-1 for CPU
    pipe = pipeline("sentiment-analysis", 
                    model=SENTIMENT_MODEL, 
                    tokenizer=SENTIMENT_MODEL, 
                    max_length=512, 
                    truncation=True,
                    device=-1)
    return pipe

def get_translation_model() -> typing.Tuple[T5Tokenizer, T5ForConditionalGeneration]:
    tokenizer = T5Tokenizer.from_pretrained(TRANSLATION_MODEL)
    model = T5ForConditionalGeneration.from_pretrained(TRANSLATION_MODEL)
    return tokenizer, model

def get_model(experiment: Experiment) -> typing.Tuple[pipeline, T5Tokenizer, T5ForConditionalGeneration]:
    tokenizer = None
    model = None
    pipe = None
    if experiment is Experiment.TRANSLATION:
        tokenizer, model = get_translation_model()
    elif experiment is Experiment.SENTIMENT:
        pipe = get_sentiment_model()
    return pipe, tokenizer, model

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

def translate(input_text: str, tokenizer: T5Tokenizer, model: T5ForConditionalGeneration) -> str:
    input_text = "translate English to French: " + input_text
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    outputs = model.generate(input_ids, max_new_tokens=1000)
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return result

def sentiment(input_text:str, pipe: pipeline) -> str:
    return pipe(input_text)[0]['label']

def get_num_cores() -> int:
    return 2