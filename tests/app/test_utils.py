import pytest
from app.utils import is_uppercase, remove_allowed_words


def test_remove_allowed_words_if_one_subreddit():
    comment_mock = "really nice comment r/subreddit"

    expected_comment = "really nice comment"

    comment = remove_allowed_words(comment_mock)

    assert comment == expected_comment


def test_remove_allowed_words_if_multiple_subreddits():
    comment_mock = (
        "r/subreddit3 really nice r/subreddit comment r/subreddit r/subreddit2"
    )

    expected_comment = "really nice comment"

    comment = remove_allowed_words(comment_mock)

    assert comment == expected_comment


def test_remove_allowed_words_if_one_username():
    comment_mock = "u/nomanoid really nice comment"

    expected_comment = "really nice comment"

    comment = remove_allowed_words(comment_mock)

    assert comment == expected_comment


def test_remove_allowed_words_if_multiple_usernames():
    comment_mock = "u/nomanoid really nice u/matoras comment"

    expected_comment = "really nice comment"

    comment = remove_allowed_words(comment_mock)

    assert comment == expected_comment


def test_is_uppercase_if_screaming():
    comment_mock = "AROOOOOOO MFERSS"

    screaming = is_uppercase(comment_mock)

    assert screaming == True


def test_is_uppercase_if_not_screaming():
    comment_mock = "Arooooo Mfers"

    screaming = is_uppercase(comment_mock)

    assert screaming == False
