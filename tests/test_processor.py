import unittest
import pandas as pd
from src.processor import DataProcessor


class TestDataProcessor(unittest.TestCase):

    def test_clean_data_removes_duplicates(self):
        processor = DataProcessor()

        df = pd.DataFrame({
            "title": ["Article 1", "Article 1"],
            "source": ["BBC", "BBC"],
            "url": ["https://example.com/1", "https://example.com/1"],
            "author": [None, None],
            "published_at": [None, None],
            "description": [None, None],
            "content": [None, None],
        })

        cleaned_df = processor.clean_data(df)

        self.assertEqual(len(cleaned_df), 1)
        self.assertEqual(cleaned_df.iloc[0]["author"], "Unknown")

    def test_clean_data_adds_missing_columns(self):
        processor = DataProcessor()
        df = pd.DataFrame({
            "title": ["Article 1"],
            "source": ["BBC"],
            "url": ["https://example.com/1"],
        })

        cleaned_df = processor.clean_data(df)
        self.assertIn("published_at", cleaned_df.columns)
        self.assertIn("content", cleaned_df.columns)


if __name__ == "__main__":
    unittest.main()
