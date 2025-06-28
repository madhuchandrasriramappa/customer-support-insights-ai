import openai
from src.config import OPENAI_API_KEY, MODEL
import time

openai.api_key = OPENAI_API_KEY

def classify_and_analyze(text):
    try:
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a support ticket classifier."},
                {"role": "user", "content": f"Classify the following support message and analyze its sentiment:\n\n{text}\n\nReturn the category and sentiment (Positive, Neutral, Negative)."}
            ]
        )
        reply = response.choices[0].message['content']
        return reply
    except Exception as e:
        print(f"Error processing OpenAI API: {e}")
        return "Category: Unknown, Sentiment: Unknown"
