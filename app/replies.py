from app.models.StoredComments import StoredComments
from app.utils import remove_allowed_words, is_uppercase


# TODO: Make a replies class which can be inherited to several types of replies
def reply_to_lowercase(subreddit, stored_comments: StoredComments):
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
            if not is_uppercase(processed_body):
                print(comment.body)
                print("CAN YOU SPEAK LOUDER MFER??")

            stored_comments.add(comment.id)
