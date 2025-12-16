from nlplogic.corenlp import summarize_wiki, get_phrases, get_text_blob
import pytest


def test_getphrases():
    assert "python" in get_phrases("Python (programming language)").lower()