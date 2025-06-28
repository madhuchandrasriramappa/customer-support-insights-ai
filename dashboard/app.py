import sys
import os
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from src.config import DB_PATH

engine = create_engine(DB_PATH)

def load_data(query):
    with engine.connect() as conn:
        return pd.read_sql(query, conn)

st.title("Customer Support Insights Dashboard")

# Tickets by Category & Sentiment
st.header("Tickets by Category & Sentiment")
cat_data = load_data("SELECT ai_analysis, COUNT(*) as count FROM tickets GROUP BY ai_analysis")
st.bar_chart(cat_data.set_index('ai_analysis'))

# Recent Negative Tickets
st.header("Recent Negative Tickets")
neg_tickets = load_data("SELECT customer_name, message, date FROM tickets WHERE ai_analysis LIKE '%Negative%' ORDER BY date DESC LIMIT 10")
st.table(neg_tickets)

# Sentiment Trend Over Time
st.header("Sentiment Trend Over Time")
trend = load_data("""
    SELECT date, ai_analysis, COUNT(*) as count
    FROM tickets
    GROUP BY date, ai_analysis
    ORDER BY date
""")
if not trend.empty:
    trend['date'] = pd.to_datetime(trend['date'])
    pivot = trend.pivot(index='date', columns='ai_analysis', values='count').fillna(0)
    st.line_chart(pivot)
else:
    st.write("No data to display.")

