from app.llm.openrouter_client import OpenRouterClient
from app.processing.map_reduce import map_reduce
from app.scraper.extractor import clean
from app.scraper.fetcher import scrape
from app.scraper.hackernews import search_hackernews
from app.schemas.research import ResearchReport  
from app.processing.research_summary import summarize_research   
from app.output.writer import save_report


def research_topic(topic: str, limit: int = 3) -> ResearchReport:
    llm = OpenRouterClient()

    articles = search_hackernews(topic, limit)

    results = []

    for article in articles:
        try:
            soup = scrape(article.url)
            text = clean(soup)

            summary = map_reduce(llm, text)

            results.append({
                "title": article.title,
                "url": article.url,
                "summary": summary,
            })

        except Exception as e:
            print(f"Failed to process {article.url}: {e}")

    if results:
        overall_summary = summarize_research(
            llm,
            [article["summary"] for article in results],
        )
    else:
        overall_summary = "No articles could be processed."

    report = ResearchReport(
    topic=topic,
    summary=overall_summary,
    articles=results,
)

    save_report(report)
    return report
