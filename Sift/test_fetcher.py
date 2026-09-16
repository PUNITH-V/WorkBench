from app.scraper.fetcher import scrape
from app.scraper.extractor import clean


url = "https://opencode.ai/"

soup = scrape(url)
text = clean(soup)

print(text[:2000])