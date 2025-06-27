# model.py
from transformers import pipeline
from datetime import datetime
import pandas as pd
import streamlit as st

@st.cache_resource
def load_classifier():
    """Load and cache the FinBERT model.
    
    Returns:
        pipeline: A sentiment analysis pipeline using the FinBERT model."""
    
    return pipeline("sentiment-analysis", model="ProsusAI/finbert", tokenizer="ProsusAI/finbert")

def classify_headline(text):
    """Classify a single headline and return label + score.
    
    Args:
        text (str): The headline text to classify.
    Returns:
        tuple: A tuple containing the sentiment label and score."""
    
    classifier = load_classifier()
    result = classifier(text)[0]
    return result['label'], result['score']

def classify_unlabelled(df):
    """Classify all unlabelled headlines in the DataFrame.
    
    Args:
        df (pd.DataFrame): DataFrame containing headlines with a 'sentiment' column.
    Returns:
        pd.DataFrame: Updated DataFrame with classified sentiments."""
    
    classifier = load_classifier()

    if 'sentiment' not in df.columns:
        df['sentiment'] = None
        
    unclassified = df[df['sentiment'].isnull()]
    if len(unclassified) == 0:
        return df, 0

    sentiments = [classifier(headline)[0]['label'] for headline in unclassified['headline']]
    df.loc[unclassified.index, 'sentiment'] = sentiments
    df.loc[unclassified.index, 'timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return df, len(unclassified)






# How this works?
# 1. The `load_classifier` function loads the FinBERT model and caches it for efficiency.
#    @st.cache_resource is used to cache the model so it doesn't reload every time the function is called.
# 2. The `classify_headline` function takes a single headline text, classifies it using the FinBERT model, and returns the sentiment label and score.
# 3. The `classify_unlabelled` function checks the DataFrame for unclassified headlines, classifies them, and updates the DataFrame with the new sentiment labels and timestamps.
#    It returns the updated DataFrame and the number of newly classified headlines.



