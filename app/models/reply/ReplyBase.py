from abc import ABC, abstractmethod

from app.models.stored_comments.StoredComments import StoredComments


class ReplyBase(ABC):
    def __init__(self, subreddit, comments_storage: str) -> None:
        self._subreddit = subreddit
        self._stored_comments = StoredComments(filename=comments_storage)

    def reply_to_new(self):
        # TODO: Keep track of the last three posts so we can delete old comments ids from posts not in new
        print("Reading comments from last 3 posts...")
        for submission in self._subreddit.new(limit=3):
            for comment in submission.comments.list():
                if comment.id in self._stored_comments:
                    continue
                
                print("Reading...")
                self._reply(comment)

                print("Adding comment to read comments")
                self._stored_comments.add(comment.id)

    @abstractmethod
    def _reply(self, comment):
        raise NotImplementedError
