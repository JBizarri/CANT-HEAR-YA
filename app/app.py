import praw

from app.config import (
    CLIENT_ID,
    CLIENT_SECRET,
    PASSWORD,
    SUBREDDIT,
    USER_AGENT,
    USERNAME,
)
from app.models.reply.ReplyToLowercase import ReplyToLowercase


def run():
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        password=PASSWORD,
        username=USERNAME,
        user_agent=USER_AGENT,
    )
    subreddit = reddit.subreddit(SUBREDDIT)

    ReplyToLowercase(subreddit, "comments.txt").reply_to_new()
