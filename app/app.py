import praw

from app.config import (CLIENT_ID, CLIENT_SECRET, PASSWORD, SUBREDDIT,
                        USER_AGENT, USERNAME)
from app.reply.ReplyToLowercase import ReplyToLowercase


def run():
    print("Connecting to reddit...")
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        password=PASSWORD,
        username=USERNAME,
        user_agent=USER_AGENT,
    )

    print("Setting subreddit to", SUBREDDIT)
    subreddit = reddit.subreddit(SUBREDDIT)

    ReplyToLowercase(subreddit, limit=10).reply_to_new()
