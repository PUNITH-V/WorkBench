from app.llm.openrouter_client import OpenRouterClient
from app.processing.map_reduce import map_reduce
from app.processing.research_summary import summarize_research
from app.scraper.extractor import clean
from app.scraper.fetcher import scrape
from app.scraper.hackernews import search_hackernews
from app.schemas.research import ResearchReport
from app.output.writer import save_report


def research_topic(
    topic: str,
    limit: int = 3,
    llm=None,
) -> ResearchReport:
    print("Searching Hacker News...")

    if llm is None:
        llm = OpenRouterClient()

    articles = search_hackernews(topic, limit)

    print(f"Found {len(articles)} articles.")

    results = []

    for article in articles:
        print(f"\nProcessing: {article.title}")

        try:
            print("  Fetching article...")
            soup = scrape(article.url)

            print("  Extracting text...")
            text = clean(soup)

            print(f"  Extracted {len(text)} characters.")

            print("  Running Map-Reduce...")
            summary = map_reduce(llm, text)

            print("  Summary complete.")

            results.append({
                "title": article.title,
                "url": article.url,
                "summary": summary,
            })

        except Exception as e:
            print(f"  Failed: {e}")

    if results:
        print("\nCreating overall research summary...")

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