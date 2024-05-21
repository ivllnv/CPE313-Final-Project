import streamlit as st
from textblob import TextBlob
import matplotlib.pyplot as plt
import pandas as pd

def sentimentAnalyzer(reviews):
    positive_count = 0
    negative_count = 0
    
    # Create an empty DataFrame
    df = pd.DataFrame(columns=['user_name', 'rating', 'review_text'])
    
    for review in reviews:
        analysis = TextBlob(review['text'])
        if analysis.sentiment.polarity > 0.01:
            positive_count += 1
        elif analysis.sentiment.polarity < -0.01:
            negative_count += 1
            
        # Append review to DataFrame
        df = df.append({'user_name': review['user']['name'], 'rating': review['rating'], 'review_text': review['text']}, ignore_index=True)
    
    # Visualize sentiment analysis
    fig, ax = plt.subplots()
    ax.bar(['Positive', 'Negative'], [positive_count, negative_count])
    st.pyplot(fig)
    
    # Display DataFrame
    st.write(df)