import json
import random
import argparse
import csv

def extract_to_tsv(json_file, out_file, num_posts):
    # Open and load the JSON data
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    if isinstance(data, list):
        posts = data  
    elif 'articles' in data:
        posts = data['articles']  
    else:
        raise ValueError("Unexpected JSON format. Expected a list or dictionary with an 'articles' key.")
    
    # Shuffle and select the required number of posts -- remove bias
    random.shuffle(posts)
    selected_posts = posts[:min(num_posts, len(posts))]

    # Write to TSV
    with open(out_file, 'w', newline='') as tsv_file:
        writer = csv.writer(tsv_file, delimiter='\t')
        # Write header
        writer.writerow(['Date', 'Title', 'Description', 'Code 1', 'Code 2'])

        # Write rows, filtering out posts with missing title or description
        valid_posts_count = 0
        for post in selected_posts:
            # Extract fields based on your data structure
            date = post.get('publishedAt', '')
            title = post.get('title', '')
            description = post.get('description', '')

            # Skip rows with missing title or description
            if not title or not description:
                continue
            
            writer.writerow([date, title, description, '', ''])
            valid_posts_count += 1

    print(f"Extracted {valid_posts_count} valid posts to {out_file}")

if __name__ == "__main__":
    # Argument parsing
    parser = argparse.ArgumentParser(description="Extract a random selection of articles to a TSV file.")
    parser.add_argument('-o', '--out_file', required=True, help="Output file name for the TSV file.")
    parser.add_argument('json_file', help="Input JSON file containing articles.")
    parser.add_argument('num_posts', type=int, help="Number of posts to output.")
    args = parser.parse_args()

    # Run extraction
    extract_to_tsv(args.json_file, args.out_file, args.num_posts)
