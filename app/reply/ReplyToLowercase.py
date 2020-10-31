from app.dao import fetch_responses, fetch_vocatives
import re
from random import choice

from .ReplyBase import ReplyBase


class ReplyToLowercase(ReplyBase):
    def __init__(self, subreddit, limit=3) -> None:
        self._footer = (
            "EU SOU UM ROBÔ E ESSA AÇÃO FOI FEITA AUTOMATICAMENTE\n\n"
            "[GITHUB](https://github.com/JBizarri/CANT-HEAR-YA) | [U/JEFFEWWASTAKEN](https://www.reddit.com/user/JeffewWasTaken)"
        )

        self._regexes = {
            "urls": r"(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])?",
            "subreddits": r"\s?r/\w+$|r/\w+\s?|\s?r/\w+",
            "users": r"\s?u/\w+$|u/\w+\s?|\s?u/\w+",
        }

        super().__init__(subreddit, limit)

    def _reply(self, comment):
        processed_body = self._parse_comment(comment.body)
        if not self._is_uppercase(processed_body):
            print(f"Replying to {comment.author.name}...")
            message = self._get_random_message()
            comment.reply(message)

    def _parse_comment(self, text: str):
        """Remove words that are allowed to be lowercase

        Args:
            text (str): String to remove words from

        Returns:
            # str: String without the allowed lowercase words
        """
        for regex in self._regexes.values():
            text = re.sub(regex, "", text)

        text = text.replace("\n", " ")

        return text

    def _get_random_message(self):
        messages = self._fetch_responses()
        vocatives = self._fetch_vocatives()

        message = choice(messages).replace("\\n", "\n")
        vocative = choice(vocatives)

        body = message.format(vocative)

        return f"{body}\n\n{self._footer}"

    def _fetch_responses(self):
        responses = fetch_responses(self._psql)

        return [response["response"] for response in responses]

    def _fetch_vocatives(self):
        vocatives = fetch_vocatives(self._psql)

        return [vocative["vocative"] for vocative in vocatives]

    @staticmethod
    def _is_uppercase(text: str):
        """Check if some string is not all uppercase

        Args:
            text (str): String to check

        Returns:
            bool: True if string is ALL uppercase. Otherwise False
        """
        # TODO: Make so if the majority of the text is uppercase return True
        return text.upper() == text
