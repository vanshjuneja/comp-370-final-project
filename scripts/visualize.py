import matplotlib.pyplot as plt

# JSON data
data = {
    "Background": {
        "Top_TF-IDF_scores": {
            "transcript": 0.01990843854697839,
            "alpha": 0.01990843854697839,
            "releases": 0.01990843854697839,
            "drawing": 0.01990843854697839,
            "presidency": 0.018310204811135163,
            "medical": 0.018310204811135163,
            "contrast": 0.012206803207423442,
            "report": 0.011262919669671233,
            "suddenly": 0.009954219273489195,
            "pauses": 0.009954219273489195
        }
    },
    "Campaign Strategy": {
        "Top_TF-IDF_scores": {
            "fox": 0.012439331256310086,
            "snl": 0.008292887504206724,
            "news": 0.007680794670044988,
            "interview": 0.007276542318989989,
            "day": 0.007145601073691146,
            "bret": 0.006910739586838936,
            "baier": 0.006910739586838936,
            "closing": 0.005476631548694466,
            "argument": 0.005476631548694466,
            "night": 0.005476631548694466
        }
    },
    "Endorsements": {
        "Top_TF-IDF_scores": {
            "endorses": 0.02904729514960157,
            "houston": 0.01681685508661144,
            "backing": 0.013759245070863903,
            "eminem": 0.012230440062990136,
            "endorse": 0.012230440062990136,
            "prominently": 0.010701635055116369,
            "beyoncé": 0.01064560516218346,
            "jennifer": 0.009172830047242602,
            "weigh": 0.009172830047242602,
            "billionaires": 0.008436442489772173
        }
    },
    "Insult/Controversy": {
        "Top_TF-IDF_scores": {
            "60": 0.007764938111497529,
            "minutes": 0.007764938111497529,
            "fascist": 0.007764938111497529,
            "using": 0.005823703583623148,
            "mel": 0.005823703583623148,
            "gibson": 0.005823703583623148,
            "iq": 0.005823703583623148,
            "right": 0.005823703583623148,
            "elon": 0.005823703583623148,
            "tries": 0.005823703583623148
        }
    },
    "Policy": {
        "Top_TF-IDF_scores": {
            "crypto": 0.01990843854697839,
            "economy": 0.01990843854697839,
            "fracking": 0.01327229236465226,
            "keep": 0.01327229236465226,
            "bitcoin": 0.01327229236465226,
            "compare": 0.01327229236465226,
            "might": 0.01327229236465226,
            "expand": 0.01327229236465226,
            "taxes": 0.01327229236465226,
            "market": 0.012206803207423442
        }
    },
    "Public Opinion": {
        "Top_TF-IDF_scores": {
            "poll": 0.031656527724877294,
            "among": 0.010552175908292433,
            "viewers": 0.0063313055449754595,
            "hispanic": 0.0063313055449754595,
            "lead": 0.0063313055449754595,
            "point": 0.0063313055449754595,
            "win": 0.005714994421577876,
            "news": 0.005253375958998596,
            "polls": 0.005176029628589445,
            "fox": 0.004898566647066751
        }
    }
}

# Plot each category as a bar chart and save
for category, details in data.items():
    scores = details["Top_TF-IDF_scores"]
    labels = list(scores.keys())
    values = list(scores.values())

    plt.figure(figsize=(10, 6))
    plt.bar(labels, values)
    plt.title(f"Top TF-IDF Scores for {category}", fontsize=16)
    plt.xlabel("Keywords", fontsize=12)
    plt.ylabel("TF-IDF Scores", fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Save each chart as an image with unique name
    plt.savefig(f"{category.replace('/', '_')}_tf_idf_chart.png")
    plt.close()

print("All charts have been saved as PNG files.")
