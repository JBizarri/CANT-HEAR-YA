import praw

from app.config import (
    CLIENT_ID,
    CLIENT_SECRET,
    PASSWORD,
    SUBREDDIT,
    USER_AGENT,
    USERNAME,
)
from app.models.StoredComments import StoredComments
from app.replies import reply_to_lowercase


def run():
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        password=PASSWORD,
        username=USERNAME,
        user_agent=USER_AGENT,
    )
    subreddit = reddit.subreddit(SUBREDDIT)

    stored_comments = StoredComments()
    reply_to_lowercase(subreddit, stored_comments)
