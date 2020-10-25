import os

COMMENTS_FILE = "comments.txt"

CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]
PASSWORD = os.environ["PASSWORD"]
USERNAME = os.environ["USERNAME"]
USER_AGENT = os.environ["USER_AGENT"]
SUBREDDIT = os.environ['SUBREDDIT']

# RegEx for finding subreddits (r/name) and usernames (u/name)
ALLOWED_LOWERCASE = [r"\s?r/\w+$|r/\w+\s?|\s?r/\w+", r"\s?u/\w+$|u/\w+\s?|\s?u/\w+"]
