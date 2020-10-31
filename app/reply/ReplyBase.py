from abc import ABC, abstractmethod

from app.dao import delete_old_comments, fetch_comments, insert_comments
from app.psql.Psql import Psql
from app.config import USERNAME


class ReplyBase(ABC):
    def __init__(self, subreddit, limit=3) -> None:
        self._subreddit = subreddit
        self._limit = limit
        self._psql = Psql()

    def reply_to_new(self):
        stored_comments = self._fetch_comments()

        new_comments = dict()
        print(f"Reading comments from last {self._limit} posts...")
        for submission in self._subreddit.new(limit=self._limit):
            for comment in submission.comments.list():

                if comment.author.name == USERNAME:
                    continue

                if comment.id in stored_comments:
                    new_comments[comment.id] = False
                    continue

                print(f"URL: https://www.reddit.com{comment.permalink}")
                self._reply(comment)

                new_comments[comment.id] = True

        self._delete_old_comments(new_comments)
        self._insert_comments(new_comments)

    @abstractmethod
    def _reply(self, comment):
        pass

    def _fetch_comments(self):
        print("Fetching Comments' IDs from DB")
        result = fetch_comments(self._psql)
        if result is None:
            return list()

        return [comment[0] for comment in result]

    def _delete_old_comments(self, new):
        result = delete_old_comments(self._psql, tuple(new.keys()))
        if not result:
            print(f"Delete old Comments' IDs status message: {result}")

    def _insert_comments(self, comments):
        param = [(id_,) for id_, new in comments.items() if new]
        if param:
            result = insert_comments(self._psql, param)
            print(f"Insert new Comments' IDs status message: {result}")
        else:
            print("No new Comments' IDs")
