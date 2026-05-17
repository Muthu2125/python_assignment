import requests
from bs4 import BeautifulSoup


class ArticleScraper:
    """
    Scrapes extra information from article webpages.
    Ethical note: this scraper only requests public article pages and uses a clear User-Agent.
    """

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 NewsAggregatorStudentProject/1.0"
        }

    def scrape_article_content(self, url):
        if not url or url == "Unknown":
            return "No URL available for scraping."

        try:
            response = requests.get(url, headers=self.headers, timeout=8)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            # Remove scripts and style blocks to keep scraped text clean.
            for tag in soup(["script", "style", "noscript"]):
                tag.decompose()

            paragraphs = soup.find_all("p")
            text = " ".join([p.get_text(strip=True) for p in paragraphs])
            text = " ".join(text.split())

            if len(text) > 1000:
                text = text[:1000] + "..."

            return text if text else "No additional content found."

        except Exception as error:
            return f"Scraping failed: {error}"
