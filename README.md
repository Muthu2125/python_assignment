# News Information Aggregator

## Project Overview

This project is a Python Information Aggregator that collects current news articles using a public News API and then applies web scraping to collect additional article content from the article webpages. The application includes a Tkinter GUI, data cleaning, duplicate removal, CSV export, data visualisation, object-oriented programming, and unit testing.

## Features

- Fetches current news articles from NewsAPI
- Allows users to choose a category such as business, technology, sports, health, science, or entertainment
- Scrapes extra article text from article webpages using BeautifulSoup
- Cleans data and removes duplicate articles
- Saves processed results into `data/articles.csv`
- Provides charts for article distribution by source and author availability
- Uses OOP concepts including encapsulation, inheritance, abstraction, and polymorphism
- Includes unit tests using `unittest`
- Provides a simple Tkinter GUI for user interaction

## Folder Structure

```text
news_information_aggregator/
│
├── main.py
├── config.py
├── requirements.txt
├── README.md
├── report.md
├── .env.example
│
├── src/
│   ├── __init__.py
│   ├── article.py
│   ├── api_fetcher.py
│   ├── scraper.py
│   ├── processor.py
│   ├── visualizer.py
│   └── gui.py
│
├── tests/
│   ├── __init__.py
│   ├── test_article.py
│   └── test_processor.py
│
├── csv output /
└── screenshots/
```

## Setup Instructions

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Create a NewsAPI key

Create a free API key from NewsAPI.

### 3. Create `.env` file

Copy `.env.example` and rename it to `.env`.

Then update it like this:

```env
NEWS_API_KEY=your_actual_api_key_here
```

### 4. Run the application

```bash
python main.py
```

### 5. Run unit tests

```bash
python -m unittest discover tests
```

## Ethical Web Scraping Note

This project only scrapes publicly available webpages and uses a clear User-Agent. It is designed for educational use only. Users should respect the terms of service of NewsAPI and the news websites being accessed.

## OOP Design

- `NewsArticle` represents the article data entity.
- `BaseFetcher` is an abstract parent class.
- `NewsAPIFetcher` inherits from `BaseFetcher` and implements `fetch_articles()`.
- `ArticleScraper` handles webpage scraping.
- `DataProcessor` handles cleaning, duplicate removal and CSV export.
- `NewsVisualizer` creates charts.
- `NewsAggregatorGUI` manages the user interface.

## Limitations

Some websites block scraping or load content dynamically using JavaScript. When this happens, the application handles the error and continues running.
