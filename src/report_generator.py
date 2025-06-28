import pandas as pd
from src.db_operations import run_query

def generate_summary_reports():
    reports = {}

    # 1. Count of tickets by category
    category_query = """
    SELECT ai_analysis, COUNT(*) AS count
    FROM tickets
    GROUP BY ai_analysis;
    """
    reports['tickets_by_category'] = pd.DataFrame(run_query(category_query), columns=["Category & Sentiment", "Count"])

    # 2. Recent negative sentiment tickets
    negative_query = """
    SELECT * FROM tickets
    WHERE ai_analysis LIKE '%Negative%'
    ORDER BY date DESC
    LIMIT 10;
    """
    reports['recent_negative'] = pd.DataFrame(run_query(negative_query))

    # 3. Sentiment trend over time
    trend_query = """
    SELECT date, ai_analysis, COUNT(*) AS count
    FROM tickets
    GROUP BY date, ai_analysis
    ORDER BY date;
    """
    reports['sentiment_trend'] = pd.DataFrame(run_query(trend_query), columns=["Date", "Sentiment", "Count"])

    return reports

def export_reports_to_csv(reports: dict, output_dir: str = "data/outputs"):
    for name, df in reports.items():
        df.to_csv(f"{output_dir}/{name}.csv", index=False)
        print(f"✅ Report saved: {output_dir}/{name}.csv")

if __name__ == "__main__":
    reports = generate_summary_reports()
    export_reports_to_csv(reports)
