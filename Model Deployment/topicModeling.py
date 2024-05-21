from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import streamlit as st

def topic_modeling(reviews):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(reviews)
    lda = LatentDirichletAllocation(n_components=5, random_state=42)
    lda.fit(X)
    # Get top words by sentiment
    for idx, topic in enumerate(lda.components_):
        st.write(f"Top words for Topic {idx}:")
        st.write([vectorizer.get_feature_names_out()[i] for i in topic.argsort()[:-11:-1]])
