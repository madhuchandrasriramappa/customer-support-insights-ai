import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DB_PATH = os.getenv("DB_URL", "sqlite:///../db/support_tickets.db")
MODEL = "gpt-3.5-turbo"
