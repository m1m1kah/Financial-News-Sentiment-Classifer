import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from model import classify_headline

st.set_page_config(page_title="Financial Sentiment Dashboard", layout="centered")

st.title("📰 Financial Sentiment Dashboard")

# Load data
try:
    df = pd.read_csv("classified_headlines.csv")
    # Standardize column names
    df = df.rename(columns={
        'headline': 'Headline',
        'timestamp': 'Date',
        'sentiment': 'Sentiment'
    })

except FileNotFoundError:
    st.error("classified_headlines.csv not found.")
    st.stop()

# Check required columns
required_cols = {'Date', 'Headline', 'Sentiment'}
if not required_cols.issubset(df.columns):
    st.error(f"Missing columns. Required: {required_cols}")
    st.stop()

# Convert date
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df.dropna(subset=['Date'], inplace=True)

#Pie chart for sentiment breakdown
# Count sentiments
sentiment_counts = df['Sentiment'].value_counts().reset_index() # counts the occurrences of each sentiment i.e 5 positive, 3 negative, etc.
sentiment_counts.columns = ['Sentiment', 'Count'] # renaming the columns to Sentiment and Count

st.subheader("📊 Sentiment Breakdown")

fig, ax = plt.subplots(figsize=(4, 4))
ax.pie(
    sentiment_counts['Count'],
    labels=sentiment_counts['Sentiment'],
    autopct='%1.1f%%',
    startangle=90,
    colors=['#4CAF50', '#FFC107', '#F44336']
)
ax.axis('equal')
ax.set_title("Sentiment Distribution")
st.pyplot(fig)



# Code that shows the sentiment breakdown by date
st.subheader("📈 Sentiment Over Time")

daily_sentiment = (
    df.groupby([df['Date'].dt.date, 'Sentiment'])
    .size()
    .unstack(fill_value=0)
    .sort_index()
)

st.line_chart(daily_sentiment)

# Code that shows the most recent headlines with sentiment
with st.expander("🔍 Preview Headline Data"):
    st.dataframe(df[['Date', 'Headline', 'Sentiment']].sort_values("Date", ascending=False))

# Classifying user's input headline
st.subheader("📝 Classify Your Headline")
user_input = st.text_area("Enter a headline to classify:")
if st.button("Classify"):
    if user_input:
        label, score = classify_headline(user_input)
        st.success(f"Sentiment: {label} (Score: {score:.2f})")
    else:
        st.warning("Please enter a headline to classify.")




# How this works
# 1. The app reads the classified headlines from `classified_headlines.csv`.
# 2. It checks for required columns and converts the date column to datetime format.
# 3. It creates a pie chart showing the sentiment distribution using Matplotlib.
# 4. It generates a line chart showing sentiment trends over time.
# 5. It displays the most recent headlines with their sentiments in a table.
# 6. It allows users to input a headline and classify it using the FinBERT model.

# Note:
# - The app uses Streamlit for the web interface, Matplotlib for plotting, and Pandas for data manipulation.
# - The `classify_headline` function is imported from the `model.py` file
