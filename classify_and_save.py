import pandas as pd
from model import classify_unlabelled
import os

# Load today's scraped headlines
df = pd.read_csv("news_headlines.csv")

# Ensure sentiment column exists
if 'sentiment' not in df.columns:
    df['sentiment'] = None

# Classify only unlabelled headlines
df, n_classified = classify_unlabelled(df)

# Load existing classified data if file exists
classified_file = "classified_headlines.csv"
if os.path.exists(classified_file):
    old_df = pd.read_csv(classified_file)
    
    # Combine and drop duplicates based on headline
    combined_df = pd.concat([old_df, df], ignore_index=True) # Concatenate old and new data
    combined_df.drop_duplicates(subset="headline", inplace=True)
else:
    combined_df = df

# Save updated dataset
combined_df.to_csv(classified_file, index=False)

print(f"Classified {n_classified} new headlines and updated '{classified_file}' with {len(combined_df)} total entries.")

# How this works
# 1. Load today's scraped headlines from "news_headlines.csv".
# 2. Ensure the 'sentiment' column exists in the DataFrame.
# 3. Classify only the unlabelled headlines using the `classify_unlabelled` function.
# 4. If "classified_headlines.csv" exists, load it and combine it with today's classified headlines.
# 5. Drop duplicates based on the 'headline' column to ensure unique entries.
# 6. Save the combined DataFrame back to "classified_headlines.csv".


