import pandas as pd
from transformers import pipeline

# Model
MODEL = "cardiffnlp/twitter-roberta-base-sentiment-latest"

# Data
splits = {'train': 'train_df.csv', 'validation': 'val_df.csv', 'test': 'test_df.csv'}
CSV_DATA = "hf://datasets/rahmaabusalma/tweets_sentiment_analysis/" + splits["test"]


def get_model():
    # Load model directly
    # device=-1 for CPU
    pipe = pipeline("sentiment-analysis", 
                    model=MODEL, 
                    tokenizer=MODEL, 
                    max_length=512, 
                    truncation=True,
                    device=-1)
    return pipe

def get_dataset():
    df = pd.read_csv(CSV_DATA)
    return list(df['text'].values)

def get_num_cores():
    return 4