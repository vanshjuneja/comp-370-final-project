import json
import os
import sys

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))
sys.path.append(src_path)

from dataCollection import *

def getApiKey():
     # Get secret key
    secretKeyDir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
    secrets_path = os.path.join(secretKeyDir, 'api_key.json')
    
    # Open the secrets.json file and load its contents
    with open(secrets_path, 'r') as secrets_file:
        secrets = json.load(secrets_file)
        apiKey= secrets["secret_key"]

    return apiKey

def saveArticlesFromPastMonth(apiKey):
    # Dates to fetch articles from
    dates = ["2024-10-11", "2024-10-12", "2024-10-13", "2024-10-14", "2024-10-15", "2024-10-16", "2024-10-17", "2024-10-18", 
             "2024-10-19", "2024-10-20", "2024-10-21", "2024-10-22", "2024-10-23", "2024-10-24", "2024-10-25", "2024-10-26", 
             "2024-10-27", "2024-10-28", "2024-10-29", "2024-10-30", "2024-10-31", "2024-11-01", "2024-11-02", "2024-11-03" ]

    # Create a json doc for each day
    for date in dates:

        with open("data/dailyArticles/" + date + ".json", "w") as f:
            articles = fetch_latest_news(apiKey, date, date)
            json.dump(articles, f)
            f.close()

def main():
    apiKey = getApiKey()

    saveArticlesFromPastMonth(apiKey)
    



if __name__ == "__main__":
    main()