# comp-370-final-project

## Research question

Media portrayal of Kamala Harris and its potential impact on her election loss.

What proportion of North American media coverage on Kamala Harris in the month leading up to the recent election exhibits a positive, negative, or neutral tone, and what recurring political topics (like immigration policy, economic reform, etc) are most prominent within each sentiment category?
Additionally, how does the frequency and intensity of negative coverage across these topics correlate with her declining public support as the election approached?

## Data collection

- `script/fetchNewsArticle.py` collects 20 of the most relevant articles per day between 2024-10-11 and 2024-11-03 and stores them into `data/dailyArticles`
- It then compiles them into a singular document `data/allArticles.json`
