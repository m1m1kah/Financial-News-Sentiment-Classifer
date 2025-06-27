# Financial-News-Sentiment-Classifer

This project looks at finance related headlines and classifies the sentiment of them. Stock Prices are incredibly difficult to predict as they are so heavily impacted by things like Politics, natural disasters, wars and conflict etc. Hence why NLP techniques are incredibly important in finance as it can identify potential risks and opportunities.

## The following shows a step by step breakdown of how I implemented the application: 

1. I scraped the NewsAPI to get a bunch of Finance related headlines that were then saved under news_headlines.csv (this was done in scraping.py)
2. I then created model.py which includes functions to take unclassfied news data and classify them using the FinBERT model
3. Next, under classify_and_save.py, I read in news_headlines.csv and classified the headlines (as positive / negative/ neutral) and saved this under classified_headlines.csv. 
4. app.py was a simple streamlit application that would present a pie chart of positive/ negative/ neutral headlines, a line graph of sentiment over time and an input box where a user can type in their own headline and it would return the sentiment + a confidence score
5. Finally, I used the python "os" and "schedule" libraries to automate the scraping and classification of news headlines so I can keep track of how the sentiment of Financial news changes over time. 

## Below I wanted to document some mistakes i made/ tips for the future: 

1. My code crashed as my news_headlines.csv didn't have a sentiment column and my classified_csv did and model.py expected a "sentiment" column
     - I added a if statement check to see if the sentiment column existed, and to create it if it didn't exist.
     - I did this both is classify_and_save.py and model.py so everything was more robust.
2. My old code didn't concatenate the data, it simply deleted the old data and replaced it with the new in scraping.py
     - Using pd.concat() helped with this.
     - Also using drop_duplicates helped to ensure I wasn't scraping the same headlines
3. Use if os.path.exists() to check whether a file already exists before trying to open or update it.
     - This made sure that if classified_headlines.csv doesn't exist for the first time I run the code, I don't get a FileNotFoundError. 
