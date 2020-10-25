import re

from app.config import ALLOWED_LOWERCASE


def is_uppercase(comment: str) -> bool:
    """Check if some string is not all uppercase

    Args:
        comment (str): String to check

    Returns:
        bool: True if string is NOT ALL uppercase. Otherwise False
    """
    # TODO: Make so if the majority of the text is uppercase return True
    return comment.upper() == comment


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
