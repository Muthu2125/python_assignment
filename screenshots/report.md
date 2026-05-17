# Brief Report: News Information Aggregator

## 1. Introduction

This project developed a Python-based News Information Aggregator that collects news articles from a public API and enriches the results using web scraping. The main purpose of the application is to provide users with a simple way to explore current news articles by category through a graphical interface.

## 2. Project Objective

The objective was to design an information aggregator that combines API integration, web scraping, data processing, data visualisation, object-oriented programming, unit testing and GUI development. The project focuses on current news articles because news data changes frequently and provides a practical example of real-world data aggregation.

## 3. System Design and Architecture

The system was designed using separate classes for each major responsibility. This makes the code easier to maintain, test and extend. The main classes are `NewsArticle`, `BaseFetcher`, `NewsAPIFetcher`, `ArticleScraper`, `DataProcessor`, `NewsVisualizer` and `NewsAggregatorGUI`.

## 4. API Integration

The project uses NewsAPI to fetch current news headlines and article metadata. The user can choose a preferred category from the GUI, such as business, technology, sports, health, science or entertainment. The API response is converted into `NewsArticle` objects for further processing.

## 5. Web Scraping Implementation

BeautifulSoup is used to scrape additional article text from the article URLs provided by the API. This adds richer information than the API response alone. The scraper includes exception handling because some websites block scraping or provide limited HTML content.

## 6. Data Processing and Cleaning

The `DataProcessor` class converts article objects into a pandas DataFrame. It removes duplicates based on title and URL, fills missing values with `Unknown`, trims text fields and saves the cleaned dataset as a CSV file.

## 7. Data Visualisation

The project includes visualisations using Matplotlib. The first chart shows the number of articles by source. The second chart shows whether author information is available or missing. These visualisations help users understand the structure and quality of the collected news data.

## 8. Object-Oriented Programming Principles

The project demonstrates encapsulation through the `NewsArticle` class, abstraction through the `BaseFetcher` abstract class, inheritance through `NewsAPIFetcher`, and polymorphism through the shared `fetch_articles()` method structure. This supports modularity and makes the code easier to extend in the future.

## 9. Unit Testing

Unit tests were created using the `unittest` framework. The tests check whether article objects convert correctly into dictionaries and whether the data processor removes duplicates and handles missing values correctly.

## 10. GUI Implementation

The graphical user interface was developed using Tkinter. It allows the user to select a news category, choose the number of articles, fetch news, view results and generate visual charts. This improves usability compared with a command-line-only application.

## 11. Challenges Faced

One challenge was that not all news websites allow easy scraping. Some websites block automated requests or use JavaScript to load article content. To manage this, the scraper includes error handling so that the program continues running even if one article cannot be scraped.

## 12. Ethical and Legal Considerations

The project is designed for educational use. It uses a clear User-Agent and only requests publicly available webpages. Users should respect the terms of service of NewsAPI and the websites being scraped. The application also limits the number of articles requested to reduce unnecessary load.

## 13. Additional Features

An optional feature was added that allows users to choose the number of articles to fetch. The application also saves the processed dataset to CSV, which allows further analysis after using the GUI.

## 14. Conclusion

The final application meets the main requirements of the assignment by combining API integration, web scraping, data processing, visualisation, OOP, testing and GUI interaction. The modular design allows the project to be extended with additional APIs, caching, sentiment analysis or more advanced visualisations in the future.
