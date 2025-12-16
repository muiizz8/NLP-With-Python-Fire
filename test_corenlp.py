from nlplogic.corenlp import get_phrases


def test_getphrases():
    assert "python" in get_phrases("Python (programming language)").lower()
