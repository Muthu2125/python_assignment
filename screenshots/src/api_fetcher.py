import requests
from abc import ABC, abstractmethod
from config import NEWS_API_KEY, BASE_URL, DEFAULT_COUNTRY, DEFAULT_PAGE_SIZE
from src.article import NewsArticle


class BaseFetcher(ABC):
    """
    Abstract parent class.
    Demonstrates inheritance and polymorphism because child fetchers
    must implement fetch_articles().
    """

    @abstractmethod
    def fetch_articles(self):
        pass


class NewsAPIFetcher(BaseFetcher):
    """
    Fetches news articles from NewsAPI.
    """

    def __init__(self, category="technology", country=DEFAULT_COUNTRY, page_size=DEFAULT_PAGE_SIZE):
        self.category = category
        self.country = country
        self.page_size = page_size

    def fetch_articles(self):
        if not NEWS_API_KEY:
            raise ValueError("Missing NEWS_API_KEY. Please create a .env file and add NEWS_API_KEY=your_key_here.")

        params = {
            "apiKey": NEWS_API_KEY,
            "country": self.country,
            "category": self.category,
            "pageSize": self.page_size,
        }

        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()
        articles = []

        for item in data.get("articles", []):
            article = NewsArticle(
                title=item.get("title") or "Untitled",
                source=item.get("source", {}).get("name") or "Unknown",
                url=item.get("url") or "Unknown",
                published_at=item.get("publishedAt"),
                author=item.get("author"),
                description=item.get("description"),
                content=item.get("content"),
            )
            articles.append(article)

        return articles
