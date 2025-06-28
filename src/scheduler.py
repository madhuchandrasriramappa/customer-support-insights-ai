import time
from src.data_ingestion import load_raw_data, clean_data
from src.ai_enrichment import classify_and_analyze
from src.db_operations import write_to_db
from src.report_generator import generate_summary_reports, export_reports_to_csv

def run_pipeline():
    print("🚀 Starting pipeline...")

    # Load raw data (adjust path as needed)
    df = load_raw_data("data/raw/support_tickets.csv")
    print(f"Loaded {len(df)} records.")

    # Clean data
    df = clean_data(df)
    print(f"Cleaned data; {len(df)} records remain after cleaning.")

    # Enrich with AI analysis
    print("Enriching data with OpenAI...")
    df['ai_analysis'] = df['message'].apply(classify_and_analyze)

    # Write enriched data to DB
    write_to_db(df, "tickets")
    print("Data written to DB.")

    # Generate reports and save CSVs
    reports = generate_summary_reports()
    export_reports_to_csv(reports)
    print("Reports generated and saved.")

if __name__ == "__main__":
    run_pipeline()
