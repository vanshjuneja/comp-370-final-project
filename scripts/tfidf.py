import pandas as pd
import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from collections import defaultdict
import math

nltk.download('punkt')
nltk.download('stopwords')


def preprocess_title(title):
    # Load stop words
    stop_words = set(stopwords.words('english'))
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(title)  # Tokenize the title
    filtered_tokens = [word.lower() for word in tokens if word.lower() not in stop_words]  # Remove stop words
    return filtered_tokens



def groupArticlesByCategory():
    df = pd.read_csv("data/annotated_articles.csv", on_bad_lines='skip')

    # Create a dictionary to hold the JSON structure
    category_dict = {}

    # Apply preprocessing to the title column
    df['Title'] = df['Title'].apply(preprocess_title)

    # Group by category and process
    for Topic, group in df.groupby('Topic'):
        # Create a list of [title, sentiment] for each category
        category_dict[Topic] = group[['Title', 'Sentiment']].values.tolist()

    # Write the dictionary to a JSON file
    output_path = 'data/categories.json' 
    with open(output_path, 'w', encoding='utf-8') as json_file:
        json.dump(category_dict, json_file, ensure_ascii=False, indent=4)

    print(f"JSON file has been saved to {output_path}")

def computeTF(articlesOfCategory, category, term_frequency_in_other_categories):
    term_frequency_dict = defaultdict(int)
    sentiment_dict = defaultdict(int)
    word_total = 0

    for article in articlesOfCategory:
        for word in article[0]:
            term_frequency_dict[word] += 1
            term_frequency_in_other_categories[word].add(category)
            word_total += 1
        sentiment_dict[article[1]] +=1
    
    return [term_frequency_dict, term_frequency_in_other_categories, sentiment_dict, word_total]


def computeTFIDF(term_frequency, term_frequency_in_other_categories, word_total):
    tfidf = {}
    for key, value in term_frequency.items():
        tfidf[key] = (value / word_total) * math.log(6/len(term_frequency_in_other_categories[key]))

    return tfidf


def compute_top_10_TFIDF_per_category():

    with open('data/categories.json', 'r') as f:
        articlesByCategories = json.load(f)

    term_frequency_dict = {}
    term_frequency_in_other_categories = defaultdict(set)
    sentiment_dict = {}
    word_total = {}
    tfidf = {}
    top10tfidf = defaultdict(defaultdict)

    # Compute the term_frequency for each category, the number of categories that mention a term as 
    # well as the number of pos, neg and neutral articles in each category
    for category in articlesByCategories:
        results = computeTF(articlesByCategories[category], category, term_frequency_in_other_categories)
        term_frequency_dict[category] = results[0]
        term_frequency_in_other_categories = results[1]
        sentiment_dict[category] = results[2]
        word_total[category] = results[3]

    
    # Compute the tf-idf for each category
    for category in term_frequency_dict:
        tfidf[category] = computeTFIDF(term_frequency_dict[category], term_frequency_in_other_categories, word_total[category])
    
    # Get the top 10 tf-idf scores for each category and store into a file
    for category in term_frequency_dict:
        top10tfidf[category]["Top_TF-IDF_scores"] = dict(sorted(tfidf[category].items(), key=lambda x: x[1], reverse=True)[:10])
        top10tfidf[category]["Sentiment"] = sentiment_dict[category]
    
    

    with open('data/TF_IDF.json', 'w') as outfile:
        json.dump(top10tfidf, outfile)




            

def main():
    #groupArticlesByCategory()
    compute_top_10_TFIDF_per_category()

if __name__ == "__main__":
    main()