# Dataset

## Overview
This directory contains the dataset used for this project. The primary dataset is derived from the Yelp dataset, specifically the `business.json` file, which includes detailed information about various businesses.

## Dataset Details

### `business.json`
- **Features**:
  - `business_id`: Unique identifier for the business.
  - `name`: Name of the business.
  - `address`: Street address of the business.
  - `city`: City where the business is located.
  - `state`: State where the business is located.
  - `postal_code`: Postal code of the business location.
  - `latitude`: Latitude coordinate of the business.
  - `longitude`: Longitude coordinate of the business.
  - `stars`: Average rating of the business.
  - `review_count`: Number of reviews the business has received.
  - `is_open`: Indicates whether the business is currently open.
  - `categories`: Categories associated with the business.
- **Total Records**: 209,393 businesses

### Data Preprocessing
1. Text Cleaning
2. Tokenization 
3. Removing stopwords
4. Stemming or Lemmatization
5. Feature Extraction
6. Encoding Labels

### `dataset_finals.csv`
- **Features**:
  - `review_id`: Unique identifier for each review.
  - `user_id`: Unique identifier for the user who wrote the review.
  - `business_id`: Unique identifier for the business being reviewed.
  - `stars`: Rating given by the user (integer, e.g., 1 to 5).
  - `useful`: Number of useful votes the review received (integer).
  - `funny`: Number of funny votes the review received (integer).
  - `cool`: Number of cool votes the review received (integer).
  - `text`: The actual text content of the review (string).
  - `date`: The date the review was posted (string, e.g., “2018-07-07 22:09:11”).
  - `cleanText`: Preprocessed text for sentiment analysis, where unnecessary words and characters have been removed (string).
