import matplotlib.pyplot as plt


class NewsVisualizer:
    """
    Creates visualisations for news article trends.
    """

    def plot_articles_by_source(self, df):
        if df.empty:
            print("No data available for visualisation.")
            return

        source_counts = df["source"].value_counts()

        colors = [
            "#2563EB", "#059669", "#F97316", "#7C3AED", "#DC2626",
            "#0891B2", "#CA8A04", "#DB2777", "#16A34A", "#4F46E5"
        ]

        plt.figure(figsize=(10, 5))
        source_counts.plot(
            kind="bar",
            color=colors[:len(source_counts)],
            edgecolor="#1F2937"
        )

        plt.title("Number of Articles by Source", fontsize=15, fontweight="bold")
        plt.xlabel("News Source", fontsize=11)
        plt.ylabel("Number of Articles", fontsize=11)
        plt.xticks(rotation=45, ha="right")
        plt.grid(axis="y", linestyle="--", alpha=0.4)
        plt.tight_layout()
        plt.show()

    def plot_author_availability(self, df):
        if df.empty:
            print("No data available for visualisation.")
            return

        author_status = df["author"].apply(
            lambda x: "Available" if x != "Unknown" else "Missing"
        )
        counts = author_status.value_counts()

        colors = ["#059669", "#DC2626"]

        plt.figure(figsize=(6, 5))
        counts.plot(
            kind="pie",
            autopct="%1.1f%%",
            colors=colors[:len(counts)],
            startangle=90,
            explode=[0.04] * len(counts),
            shadow=True
        )

        plt.title("Author Information Availability", fontsize=15, fontweight="bold")
        plt.ylabel("")
        plt.tight_layout()
        plt.show()