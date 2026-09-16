from pydantic import BaseModel


class ArticleSummary(BaseModel):
    title: str
    url: str
    summary: str


class ResearchReport(BaseModel):
    topic: str
    summary: str
    articles: list[ArticleSummary]