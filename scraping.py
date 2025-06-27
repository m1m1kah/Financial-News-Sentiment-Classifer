import os
from bs4 import BeautifulSoup
import requests

from newsapi import NewsApiClient
import pandas as pd
from datetime import datetime

# Initialize NewsAPI client
api_key = '1fe4577a0c384a05a60fcefa4bd4039f'
newsapi = NewsApiClient(api_key=api_key)

# Get top business headlines
articles = newsapi.get_top_headlines(category="business", language="en", page_size=10, country="us")

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
new_rows = [
    {"headline": article["title"], "timestamp": timestamp}
    for article in articles["articles"]
]

new_df = pd.DataFrame(new_rows)

# File path
file_path = "news_headlines.csv"

# Append if file exists
if os.path.exists(file_path):
    old_df = pd.read_csv(file_path)
    combined_df = pd.concat([old_df, new_df], ignore_index=True)

    # Optional: drop duplicates based on headline
    combined_df.drop_duplicates(subset="headline", inplace=True)

    combined_df.to_csv(file_path, index=False)
else:
    new_df.to_csv(file_path, index=False)

print(f"Saved {len(new_df)} new headlines.")


