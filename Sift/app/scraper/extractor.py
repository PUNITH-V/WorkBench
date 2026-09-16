import trafilatura
from bs4 import BeautifulSoup


def clean(soup: BeautifulSoup) -> str:
    text = trafilatura.extract(
        str(soup),
        include_comments=False,
        include_links=False,
    )

    if not text:
        text = soup.get_text(separator=" ")

    return text.strip()