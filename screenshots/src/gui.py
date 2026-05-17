import tkinter as tk
from tkinter import ttk, messagebox
from src.api_fetcher import NewsAPIFetcher
from src.scraper import ArticleScraper
from src.processor import DataProcessor
from src.visualizer import NewsVisualizer


class NewsAggregatorGUI:
    """
    Tkinter GUI for the news aggregator.
    This version uses improved layout, colours, hover effects,
    and coloured article display for a more professional interface.
    """

    def __init__(self, root):
        self.root = root
        self.root.title("News Information Aggregator")
        self.root.geometry("1100x700")
        self.root.configure(bg="#F3F6FA")

        self.processor = DataProcessor()
        self.visualizer = NewsVisualizer()
        self.df = None

        self.create_styles()
        self.create_widgets()

    def create_styles(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Custom.TCombobox",
            fieldbackground="#FFFFFF",
            background="#DCE9F9",
            foreground="#1F2937",
            arrowcolor="#2563EB",
            bordercolor="#93C5FD",
            lightcolor="#BFDBFE",
            darkcolor="#60A5FA",
            padding=6
        )

        style.configure(
            "Custom.TSpinbox",
            fieldbackground="#FFFFFF",
            background="#DCE9F9",
            foreground="#1F2937",
            bordercolor="#93C5FD",
            padding=6
        )

    def create_widgets(self):
        # Main title
        title_label = tk.Label(
            self.root,
            text="News Information Aggregator",
            font=("Arial", 24, "bold"),
            bg="#F3F6FA",
            fg="#1E3A8A"
        )
        title_label.pack(pady=(20, 5))

        subtitle_label = tk.Label(
            self.root,
            text="Fetch, scrape, clean and visualise current news articles",
            font=("Arial", 11),
            bg="#F3F6FA",
            fg="#475569"
        )
        subtitle_label.pack(pady=(0, 15))

        # Top control panel
        main_control_frame = tk.Frame(
            self.root,
            bg="#FFFFFF",
            bd=0,
            highlightbackground="#CBD5E1",
            highlightthickness=1
        )
        main_control_frame.pack(fill="x", padx=25, pady=10)

        main_control_frame.columnconfigure(0, weight=1)
        main_control_frame.columnconfigure(1, weight=1)
        main_control_frame.columnconfigure(2, weight=1)

        # Left section: Category and number of articles
        left_frame = tk.Frame(main_control_frame, bg="#FFFFFF")
        left_frame.grid(row=0, column=0, sticky="w", padx=20, pady=18)

        category_label = tk.Label(
            left_frame,
            text="Category",
            font=("Arial", 10, "bold"),
            bg="#FFFFFF",
            fg="#334155"
        )
        category_label.grid(row=0, column=0, sticky="w", pady=(0, 4))

        self.category_var = tk.StringVar(value="technology")
        self.category_dropdown = ttk.Combobox(
            left_frame,
            textvariable=self.category_var,
            values=[
                "business",
                "technology",
                "sports",
                "health",
                "science",
                "entertainment"
            ],
            state="readonly",
            width=22,
            style="Custom.TCombobox"
        )
        self.category_dropdown.grid(row=1, column=0, padx=(0, 15))

        article_label = tk.Label(
            left_frame,
            text="No. of Articles",
            font=("Arial", 10, "bold"),
            bg="#FFFFFF",
            fg="#334155"
        )
        article_label.grid(row=0, column=1, sticky="w", pady=(0, 4))

        self.article_count_var = tk.IntVar(value=10)
        self.article_spinbox = tk.Spinbox(
            left_frame,
            from_=1,
            to=20,
            textvariable=self.article_count_var,
            width=8,
            font=("Arial", 10),
            bg="#FFFFFF",
            fg="#1F2937",
            highlightbackground="#93C5FD",
            highlightcolor="#2563EB",
            buttonbackground="#DBEAFE",
            relief="solid",
            bd=1
        )
        self.article_spinbox.grid(row=1, column=1, sticky="w")

        # Centre section: Fetch button
        centre_frame = tk.Frame(main_control_frame, bg="#FFFFFF")
        centre_frame.grid(row=0, column=1, pady=18)

        self.fetch_button = tk.Button(
            centre_frame,
            text="Fetch News",
            command=self.fetch_news,
            font=("Arial", 12, "bold"),
            bg="#2563EB",
            fg="white",
            activebackground="#1D4ED8",
            activeforeground="white",
            padx=25,
            pady=10,
            relief="flat",
            cursor="hand2"
        )
        self.fetch_button.pack()

        self.add_hover_effect(self.fetch_button, "#2563EB", "#1E40AF")

        # Right section: Chart buttons
        right_frame = tk.Frame(main_control_frame, bg="#FFFFFF")
        right_frame.grid(row=0, column=2, sticky="e", padx=20, pady=18)

        self.source_chart_button = tk.Button(
            right_frame,
            text="Show Source Chart",
            command=self.show_source_chart,
            font=("Arial", 10, "bold"),
            bg="#059669",
            fg="white",
            activebackground="#047857",
            activeforeground="white",
            padx=15,
            pady=8,
            relief="flat",
            cursor="hand2"
        )
        self.source_chart_button.grid(row=0, column=0, padx=5)

        self.author_chart_button = tk.Button(
            right_frame,
            text="Show Author Chart",
            command=self.show_author_chart,
            font=("Arial", 10, "bold"),
            bg="#7C3AED",
            fg="white",
            activebackground="#6D28D9",
            activeforeground="white",
            padx=15,
            pady=8,
            relief="flat",
            cursor="hand2"
        )
        self.author_chart_button.grid(row=0, column=1, padx=5)

        self.add_hover_effect(self.source_chart_button, "#059669", "#065F46")
        self.add_hover_effect(self.author_chart_button, "#7C3AED", "#5B21B6")

        # Status label
        self.status_label = tk.Label(
            self.root,
            text="Ready. Select a category and click Fetch News.",
            font=("Arial", 10),
            bg="#F3F6FA",
            fg="#475569"
        )
        self.status_label.pack(pady=(5, 5))

        # Results box area
        results_frame = tk.Frame(
            self.root,
            bg="#FFFFFF",
            bd=0,
            highlightbackground="#CBD5E1",
            highlightthickness=1
        )
        results_frame.pack(fill="both", expand=True, padx=25, pady=15)

        results_title = tk.Label(
            results_frame,
            text="Fetched News Results",
            font=("Arial", 14, "bold"),
            bg="#FFFFFF",
            fg="#1E3A8A"
        )
        results_title.pack(anchor="w", padx=15, pady=(12, 5))

        self.results_box = tk.Text(
            results_frame,
            height=25,
            width=120,
            font=("Consolas", 10),
            bg="#F8FAFC",
            fg="#111827",
            wrap="word",
            relief="flat",
            padx=12,
            pady=12
        )
        self.results_box.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        # Scrollbar
        scrollbar = tk.Scrollbar(self.results_box)
        scrollbar.pack(side="right", fill="y")
        self.results_box.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.results_box.yview)

        # Text colours / tags
        self.results_box.tag_configure("title", foreground="#1D4ED8", font=("Consolas", 11, "bold"))
        self.results_box.tag_configure("source", foreground="#047857", font=("Consolas", 10, "bold"))
        self.results_box.tag_configure("author", foreground="#7C3AED")
        self.results_box.tag_configure("date", foreground="#EA580C")
        self.results_box.tag_configure("url", foreground="#0891B2")
        self.results_box.tag_configure("content", foreground="#374151")
        self.results_box.tag_configure("line", foreground="#94A3B8")
        self.results_box.tag_configure("status", foreground="#DC2626", font=("Consolas", 10, "bold"))

    def add_hover_effect(self, button, normal_color, hover_color):
        button.bind("<Enter>", lambda event: button.config(bg=hover_color))
        button.bind("<Leave>", lambda event: button.config(bg=normal_color))

    def fetch_news(self):
        try:
            category = self.category_var.get()
            page_size = int(self.article_count_var.get())

            self.results_box.delete("1.0", tk.END)
            self.results_box.insert(
                tk.END,
                "Fetching news and scraping article pages. Please wait...\n",
                "status"
            )
            self.status_label.config(
                text="Fetching news... Please wait.",
                fg="#EA580C"
            )
            self.root.update_idletasks()

            fetcher = NewsAPIFetcher(category=category, page_size=page_size)
            scraper = ArticleScraper()

            articles = fetcher.fetch_articles()

            for article in articles:
                if article.url:
                    article.content = scraper.scrape_article_content(article.url)

            self.df = self.processor.articles_to_dataframe(articles)
            self.df = self.processor.clean_data(self.df)
            self.processor.save_to_csv(self.df)

            self.display_results()

            self.status_label.config(
                text=f"Success: {len(self.df)} articles fetched for '{category}'.",
                fg="#047857"
            )

            messagebox.showinfo(
                "Success",
                "News articles fetched, scraped, cleaned and saved successfully."
            )

        except Exception as error:
            self.status_label.config(
                text="Error occurred. Please check API key or internet connection.",
                fg="#DC2626"
            )
            messagebox.showerror("Error", str(error))

    def display_results(self):
        self.results_box.delete("1.0", tk.END)

        if self.df is None or self.df.empty:
            self.results_box.insert(tk.END, "No articles found.", "status")
            return

        for index, row in self.df.iterrows():
            self.results_box.insert(tk.END, f"Article {index + 1}\n", "source")
            self.results_box.insert(tk.END, f"Title: {row['title']}\n", "title")
            self.results_box.insert(tk.END, f"Source: {row['source']}\n", "source")
            self.results_box.insert(tk.END, f"Author: {row['author']}\n", "author")
            self.results_box.insert(tk.END, f"Published: {row['published_at']}\n", "date")
            self.results_box.insert(tk.END, f"URL: {row['url']}\n", "url")

            content_preview = str(row.get("content", "No content available."))
            if len(content_preview) > 350:
                content_preview = content_preview[:350] + "..."

            self.results_box.insert(tk.END, f"Scraped Content Preview: {content_preview}\n", "content")
            self.results_box.insert(tk.END, "-" * 120 + "\n\n", "line")

    def show_source_chart(self):
        if self.df is None or self.df.empty:
            messagebox.showwarning("No Data", "Please fetch news first.")
            return

        self.visualizer.plot_articles_by_source(self.df)

    def show_author_chart(self):
        if self.df is None or self.df.empty:
            messagebox.showwarning("No Data", "Please fetch news first.")
            return

        self.visualizer.plot_author_availability(self.df)