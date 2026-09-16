from app.scraper.hackernews import search_hackernews
from app.scraper.fetcher import scrape
from app.scraper.extractor import clean


print("Searching Hacker News...")

articles = search_hackernews("AI agents", limit=1)

article = articles[0]

print(f"Article: {article.title}")
print(f"URL: {article.url}")

print("\nFetching...")
soup = scrape(article.url)

print("Fetched.")

print("\nExtracting...")
text = clean(soup)


print(f"Extracted {len(text)} characters.")
print(f"Estimated chunks: {(len(text) + 3499) // 3500}")

print("\nFirst 500 characters:")
print(text[:500])

print("\nLast 500 characters:")
print(text[-500:])