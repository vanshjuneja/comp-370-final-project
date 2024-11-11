# comp-370-final-project

## Research question

Media portrayal of Kamala Harris and its potential impact on her election loss.

What proportion of North American media coverage on Kamala Harris in the month leading up to the recent election exhibits a positive, negative, or neutral tone, and what recurring political topics (like immigration policy, economic reform, etc) are most prominent within each sentiment category?
Additionally, how does the frequency and intensity of negative coverage across these topics correlate with her declining public support as the election approached?

## Data collection

The newsApiPackage contains functions that fetch news articles.

#### Steps:

1. Fetch all English news sources from the US and save into newsSources.json
2. Filter through them to remove news sources that have a unique focus on technology, entertainment, sports and science.
