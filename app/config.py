import os

CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]
PASSWORD = os.environ["PASSWORD"]
USERNAME = os.environ["USERNAME"]
USER_AGENT = os.environ["USER_AGENT"]
SUBREDDIT = os.environ["SUBREDDIT"]

DATABASE_USER = os.environ["DATABASE_USER"]
DATABASE_URL = os.environ["DATABASE_URL"]
DATABASE_PASS = os.environ["DATABASE_PASS"]
DATABASE_PORT = os.getenv("DATABASE_PORT", 5432)
DATABASE = os.getenv("DATABASE", "postgres_db")
