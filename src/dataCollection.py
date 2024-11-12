import requests
from datetime import datetime, timedelta
import re

def fetch_latest_news(api_key, from_date, to_date):
    '''
    Queries the NewsAPI and returns a python list of english news articles (represented as dictionaries) containing 
    those news keywords and published within the last <lookback_days>

    Parameters:
    - api_key: Your NewsAPI key.
    - news_keywords: Keywords to search for.
    - lookback_days: How many days back to search for news (default: 10 days).
    
    Returns:
    - A list of news articles, where each article is represented as a dictionary.
    '''

    # NewsAPI endpoint
    url = "https://newsapi.org/v2/everything"
    
    # Define query parameters
    params = {
        'q': "Kamala Harris",              # Keywords to search for
        'searchIn': "title",               # Keyword must appear in title
        #'sources': news_source,
        'from': from_date,              
        'to': to_date,
        'language': 'en',                  # Only English articles
        'sortBy': 'popularity',            # Sort by most recent articles
        'apiKey': api_key,                  # Your NewsAPI key
        'pageSize': 21
    }
    
    # Make the GET request to the NewsAPI
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        raise Exception(f"Error querying the NewsAPI: {response.status_code, response.content}")

    articles = response.json()['articles']
    
    return articles

def fetch_all_news_sources(api_key):
    url = "https://newsapi.org/v2/top-headlines/sources"

    # Parameters for the request
    params = {
        'apiKey': api_key,
        'country': 'us',
        'language':'en'
    }

    # Make the request
    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception(f"Error querying the NewsAPI: {response.status_code}")
    
    sources = response.json()["sources"]

    return sources



    