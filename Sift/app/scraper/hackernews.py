import requests

from .models import Article


HN_SEARCH_URL = "https://hn.algolia.com/api/v1/search"


def search_hackernews(topic: str, limit: int = 3) -> list[Article]:
    params = {
        "query": topic,
        "tags": "story",
        "hitsPerPage": limit,
    }

    response = requests.get(
        HN_SEARCH_URL,
        params=params,
        timeout=10,
    )
    response.raise_for_status()

    data = response.json()

    articles = []

    for hit in data["hits"]:
        title = hit.get("title")
        url = hit.get("url")

        if not title or not url:
            continue

        articles.append(
            Article(
                title=title,
                url=url,
            )
        )

    return articles