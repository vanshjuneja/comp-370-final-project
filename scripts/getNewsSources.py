import json
import os
import sys

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))
sys.path.append(src_path)

from dataCollection import *

def main():
    # Get secret key
    secretKeyDir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
    secrets_path = os.path.join(secretKeyDir, 'api_key.json')
    
    # Open the secrets.json file and load its contents
    with open(secrets_path, 'r') as secrets_file:
        secrets = json.load(secrets_file)
        apiKey= secrets["secret_key"]

    with open("data/newsSources.json", "w") as f:
        sources = fetch_all_news_sources(apiKey)
        json.dump(sources, f)
        f.close()


if __name__ == "__main__":
    main()