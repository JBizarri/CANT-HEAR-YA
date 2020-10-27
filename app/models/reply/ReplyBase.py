from abc import ABC, abstractmethod

from app.services.sql.dao import fetchall_comments, insert_comment


class ReplyBase(ABC):
    def __init__(self, subreddit) -> None:
        self._subreddit = subreddit

    def reply_to_new(self):
        # TODO: Keep track of the last three posts so we can delete old comments ids from posts not in new
        print("Reading comments from last 3 posts...")
        comments = fetchall_comments()
        for submission in self._subreddit.new(limit=3):
            for comment in submission.comments.list():
                if comment.id in comments:
                    continue

                print("Reading...")
                self._reply(comment)

                print("Adding comment to read comments")
                insert_comment(comment.id)

    @abstractmethod
    def _reply(self, comment):
        raise NotImplementedError
