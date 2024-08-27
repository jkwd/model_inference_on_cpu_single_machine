import pandas as pd
from transformers import pipeline, T5Tokenizer, T5ForConditionalGeneration

# Model
SENTIMENT_MODEL = "cardiffnlp/twitter-roberta-base-sentiment-latest"
TRANSLATION_MODEL = "google/flan-t5-base"

# Data
splits = {'train': 'train_df.csv', 'validation': 'val_df.csv', 'test': 'test_df.csv'}
SENTIMENT_DATA = "hf://datasets/rahmaabusalma/tweets_sentiment_analysis/" + splits["test"]
TRANSLATION_DATA = "hf://datasets/Abirate/english_quotes/quotes.jsonl"

def get_sentiment_model():
    # device=-1 for CPU
    pipe = pipeline("sentiment-analysis", 
                    model=SENTIMENT_MODEL, 
                    tokenizer=SENTIMENT_MODEL, 
                    max_length=512, 
                    truncation=True,
                    device=-1)
    return pipe

def get_sentiment_dataset():
    df = pd.read_csv(SENTIMENT_DATA)
    df = df.dropna(subset=['text'])
    return list(df['text'].values)[:5]


def get_translation_model():
    tokenizer = T5Tokenizer.from_pretrained(TRANSLATION_MODEL)
    model = T5ForConditionalGeneration.from_pretrained(TRANSLATION_MODEL)
    return tokenizer, model

def get_translation_dataset():
    df = pd.read_json(TRANSLATION_DATA, lines=True)
    df = df.dropna(subset=['quote'])
    return list(df['quote'].values)[:30]

def translate(input_text, tokenizer, model):
    input_text = "translate English to French: " + input_text
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    outputs = model.generate(input_ids, max_new_tokens=1000)
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return result

def get_num_cores():
    return 2