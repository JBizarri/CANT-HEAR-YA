from abc import ABC, abstractmethod

from app.dao import delete_old_comments, fetch_comments, insert_comments
from app.psql.Psql import Psql


class ReplyBase(ABC):
    def __init__(self, subreddit) -> None:
        self._subreddit = subreddit
        self._psql = Psql()

    def reply_to_new(self):
        stored_comments = self._fetch_comments()

        new_comments = dict()
        print("Reading comments from last 3 posts...")
        for submission in self._subreddit.new(limit=3):
            for comment in submission.comments.list():

                if comment.id in stored_comments:
                    new_comments[comment.id] = False
                    continue

                print(f"Username: {comment.author.name}")
                print(f"Comment preview: {comment.body[:50]}")
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
            print(f"Deleted old Comments' IDs status message: {result}")
  
    def _insert_comments(self, comments):
        param = [(id_,) for id_, new in comments.items() if new]
        if param:
            result = insert_comments(self._psql, param)
            print(f"Insert new Comments' IDs status message: {result}")
        else:
            print("No new Comments' IDs")
