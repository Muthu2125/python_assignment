import os
import pandas as pd


class DataProcessor:
    """
    Handles conversion, cleaning, duplicate removal and saving.
    """

    def articles_to_dataframe(self, articles):
        data = [article.to_dict() for article in articles]
        return pd.DataFrame(data)

    def clean_data(self, df):
        if df.empty:
            return df

        expected_columns = ["title", "source", "url", "published_at", "author", "description", "content"]
        for column in expected_columns:
            if column not in df.columns:
                df[column] = "Unknown"

        df = df.drop_duplicates(subset=["title", "url"])
        df = df.fillna("Unknown")

        df["title"] = df["title"].astype(str).str.strip()
        df["source"] = df["source"].astype(str).str.strip()
        df["url"] = df["url"].astype(str).str.strip()
        df["has_scraped_content"] = df["content"].astype(str).str.len() > 30

        return df

    def save_to_csv(self, df, filepath="data/articles.csv"):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        df.to_csv(filepath, index=False)
