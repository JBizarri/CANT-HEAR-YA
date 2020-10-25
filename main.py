import re

import praw

from config import (
    ALLOWED_LOWERCASE,
    CLIENT_ID,
    CLIENT_SECRET,
    PASSWORD,
    SUBREDDIT,
    USER_AGENT,
    USERNAME,
)


from models.StoredComments import StoredComments


def remove_allowed_words(comment: str) -> str:
    """Remove words that are allowed to be lowercase

    Args:
        comment (str): String to remove words from

    Returns:
        # str: String without the allowed lowercase words
    """
    for allowed_word in ALLOWED_LOWERCASE:
        comment = re.sub(rf"{allowed_word}", "", comment)

    return comment


def is_whispering(comment: str) -> bool:
    """Check if some string is not all uppercase

    Args:
        comment (str): String to check

    Returns:
        bool: True if string is NOT ALL uppercase. Otherwise False
    """
    if comment.upper() != comment:
        return True

    return False


def reply_to_soft_speakers(subreddit, stored_comments: StoredComments):
    """Reply to comments that are not all uppercase in a subreddit

    Args:
        subreddit: Subreddit object from PRAW
        stored_comments (StoredComments): Manage comments that already
        have been read
    """
    # TODO: Keep track of the last three posts so we can delete old comments ids from posts not in new
    for submission in subreddit.new(limit=3):
        for comment in submission.comments.list():
            if comment.id in stored_comments:
                continue

            processed_body = remove_allowed_words(comment.body)
            # TODO: Reply to the comment with multiple responses to choose at random
            if is_whispering(processed_body):
                print(comment.body)
                print("CAN YOU SPEAK LOUDER MFER??")

            stored_comments.add(comment.id)


def main():
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        password=PASSWORD,
        username=USERNAME,
        user_agent=USER_AGENT,
    )
    subreddit = reddit.subreddit(SUBREDDIT)

    stored_comments = StoredComments()
    reply_to_soft_speakers(subreddit, stored_comments)


if __name__ == "__main__":
    main()
