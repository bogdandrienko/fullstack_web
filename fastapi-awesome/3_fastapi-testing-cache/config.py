import os
from dotenv import load_dotenv

load_dotenv()
DEBUG = True
DB_SQLITE_PATH = os.environ.get("db.db", "db.db")
