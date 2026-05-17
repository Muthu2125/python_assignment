class NewsArticle:
    """
    Represents a single news article.
    This class demonstrates encapsulation by storing article details
    as object attributes and exposing them through methods.
    """

    def __init__(self, title, source, url, published_at=None, author=None, description=None, content=None):
        self.title = title
        self.source = source
        self.url = url
        self.published_at = published_at
        self.author = author
        self.description = description
        self.content = content

    def to_dict(self):
        return {
            "title": self.title,
            "source": self.source,
            "url": self.url,
            "published_at": self.published_at,
            "author": self.author,
            "description": self.description,
            "content": self.content,
        }

    def __str__(self):
        return f"{self.title} - {self.source}"
