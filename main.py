import re

import praw

ALREADY_SEEN = list()

# RegEx for finding subreddits (r/name) and usernames (u/name)
ALLOWED_LOWERCASE = [r"\s?r/\w+$|r/\w+\s?|\s?r/\w+",
                     r"\s?u/\w+$|u/\w+\s?|\s?u/\w+"]


def remove_allowed_words(comment: str) -> str:
    """Remove words that are allowed to be lowercase

    Args:
        comment (str): String to remove words from

    Returns:
        # str: String without the allowed lowercase words
    """
    for allowed_word in ALLOWED_LOWERCASE:
        comment = re.sub(rf'{allowed_word}', "", comment)

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


def reply_to_soft_speakers(subreddit):
    """Reply to comments that are not all uppercase in a subreddit 

    Args:
        subreddit: Subreddit object from PRAW
    """
    for submission in subreddit.new(limit=3):
        for comment in submission.comments.list():
            if comment.id in ALREADY_SEEN:
                continue

            processed_body = remove_allowed_words(comment.body)
            # TODO: Reply to the comment
            # TODO: List with multiple responses to choose at random
            if is_whispering(processed_body):
                print(comment.body)
                print("CAN YOU SPEAK LOUDER MFER??")

            # TODO: Store each comment id in a file or something
            ALREADY_SEEN.append(comment.id)


def main():
    reddit = praw.Reddit('BOT')
    subreddit = reddit.subreddit("O_PACOTE")

    reply_to_soft_speakers(subreddit)


if __name__ == "__main__":
    main()
