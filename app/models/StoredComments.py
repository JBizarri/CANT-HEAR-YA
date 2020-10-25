import os

from app.config import COMMENTS_FILE


# TODO: Replace with a DB for best practice although not necessary
# TODO: Method for deleting old IDs since the main script only search in the NEW feed
# TODO: Tests for this class
class StoredComments:
    def __init__(self):
        self._path = COMMENTS_FILE

        self._create_file()

    def __contains__(self, comment_id: str) -> bool:
        """Check if a comment id is already stored

        Args:
            comment_id (str): Reddit comment's id

        Returns:
            bool: True if already stored. False otherwise
        """
        return comment_id in self._get_all_ids()

    def _create_file(self):
        """Create the comment file if not created already"""
        if not os.path.isfile(self._path):
            with open(self._path, "w") as file:
                file.write("")

    def _get_all_ids(self):
        """Get all the ids stored in the file

        Raises:
            FileNotFoundError: Raises if the file doesn't exist this is
             usually caused because the file was deleted or for some
             reason has not been create in the __init__ method

        Returns:
            list: List containing all the ids stored in the file
        """
        if os.path.isfile(self._path):
            with open(self._path, "r") as file:
                return file.read().splitlines()
        else:
            raise FileNotFoundError(self._path)

    def add(self, comment_id):
        """Add a comment id to the file

        Args:
            comment_id (str): Reddit comment's id to add

        Raises:
            FileNotFoundError: Raises if the file doesn't exist this is
            usually caused because the file was deleted or for some
            reason has not been create in the __init__ method
        """
        if os.path.isfile(self._path):
            with open(self._path, "a") as file:
                file.write(comment_id + "\n")
        else:
            raise FileNotFoundError(self._path)
