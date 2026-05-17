import unittest
from src.article import NewsArticle


class TestNewsArticle(unittest.TestCase):

    def test_article_to_dict(self):
        article = NewsArticle(
            title="Test Title",
            source="Test Source",
            url="https://example.com"
        )

        article_dict = article.to_dict()

        self.assertEqual(article_dict["title"], "Test Title")
        self.assertEqual(article_dict["source"], "Test Source")
        self.assertEqual(article_dict["url"], "https://example.com")

    def test_article_string_output(self):
        article = NewsArticle("Sample", "BBC", "https://example.com")
        self.assertEqual(str(article), "Sample - BBC")


if __name__ == "__main__":
    unittest.main()
