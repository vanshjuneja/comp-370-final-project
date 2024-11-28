import matplotlib.pyplot as plt

# JSON data
data = {
    "Background": {
        "Sentiment": {"Positive": 8, "Neutral": 15}
    },
    "Campaign Strategy": {
        "Sentiment": {"Positive": 23, "Neutral": 79, "Negative": 8}
    },
    "Endorsements": {
        "Sentiment": {"Positive": 104, "Neutral": 9, "Negative": 6}
    },
    "Insult/Controversy": {
        "Sentiment": {"Negative": 56, "Neutral": 18, "Positive": 15}
    },
    "Policy": {
        "Sentiment": {"Negative": 11, "Neutral": 18, "Positive": 1}
    },
    "Public Opinion": {
        "Sentiment": {"Negative": 36, "Neutral": 24, "Positive": 29}
    }
}

# Define consistent colors for each sentiment
colors = {
    "Positive": "#81C784",  # Green
    "Neutral": "#AEDFF7",   # Grey
    "Negative": "#FF8A80"   # Red
}

# Generate pie charts for each category
for category, details in data.items():
    sentiments = details["Sentiment"]
    labels = list(sentiments.keys())
    values = list(sentiments.values())

    # Set colors for each sentiment
    pie_colors = [colors[label] for label in labels]


    plt.figure(figsize=(8, 8))
    plt.pie(
        values,
        labels=labels,
        colors=pie_colors,
        autopct='%1.1f%%',
        startangle=140,
        explode = [0.01] * len(values)
        
    )
    plt.title(f"Sentiment Distribution for {category}", fontsize=16)
    plt.tight_layout()

    # Save the pie chart as a JPEG
    file_name = f"{category.replace('/', '_')}_sentiment_pie_chart.jpeg"
    plt.savefig(file_name, format="jpeg")
    

print("Formatted pie charts with custom colors and 3D effects have been saved as JPEG files.")
