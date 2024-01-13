import os

from dotenv import load_dotenv

load_dotenv()

DEBUG = True  # DEBUG = os.environ.get("DEBUG", True)
DB_SQLITE_PATH = os.environ.get("db.db", "db.db")
# DB_HOST = os.environ.get("DB_HOST", "127.0.0.1")
