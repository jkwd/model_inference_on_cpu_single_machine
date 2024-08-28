from enum import Enum

# Experiments
class Experiment(Enum):
    TRANSLATION = 'translation'
    SENTIMENT = 'sentiment'

# Model
SENTIMENT_MODEL = "cardiffnlp/twitter-roberta-base-sentiment-latest"
TRANSLATION_MODEL = "google/flan-t5-base"

# Data
splits = {'train': 'train_df.csv', 'validation': 'val_df.csv', 'test': 'test_df.csv'}
SENTIMENT_DATA = "hf://datasets/rahmaabusalma/tweets_sentiment_analysis/" + splits["test"]
TRANSLATION_DATA = "hf://datasets/Abirate/english_quotes/quotes.jsonl"