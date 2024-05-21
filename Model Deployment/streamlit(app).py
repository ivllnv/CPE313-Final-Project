import streamlit as st
from FetchReview import fetch_reviews
from SentimentAnalysis import sentimentAnalyzer
from topicModeling import topic_modeling
from streamlit_folium import st_folium
import folium

def main():
    st.title('Competitor Review Analysis')

    st.write("Click on the map to set the location:")
    m = folium.Map(location=[0, 0], zoom_start=1)  # Initial map with default location

    map_data = st_folium(m, width=700, height=500)

    if map_data and map_data['last_clicked']:
        latitude = map_data['last_clicked']['lat']
        longitude = map_data['last_clicked']['lng']
        st.write(f"Latitude: {latitude}, Longitude: {longitude}")

        m = folium.Map(location=[latitude, longitude], zoom_start=12)
        folium.Marker([latitude, longitude], popup=f'Lat: {latitude}, Long: {longitude}').add_to(m)
        st_folium(m, width=700, height=500)

        if st.button('Fetch Reviews'):
            reviews = fetch_reviews(latitude, longitude)
            if reviews:
                st.write('Reviews Fetched Successfully!')

                df = pd.DataFrame(reviews)

                df['sentiment'] = df['text'].apply(lambda x: 'Positive' if TextBlob(x).sentiment.polarity >= 0 else 'Negative')

                st.subheader('Reviews DataFrame')
                st.write(df)

                plot_sentiment_analysis(df['sentiment'])

                st.subheader('Topic Modeling Results')
                topic_modeling(reviews)
            else:
                st.write('Failed to fetch reviews. Please try again.')
if __name__ == "__main__":
    main()