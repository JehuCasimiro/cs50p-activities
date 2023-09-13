from twttr import shorten


def test_default_string():
    assert shorten("Twitter") == ("Twttr")


def test_upper_string():
    assert shorten("TWITTER") == ("TWTTR")


def test_lower_string():
    assert shorten("hello world!") == ("hll wrld!")


def test_digit():
    assert shorten("CS50") == ("CS50")


def test_symbols():
    assert shorten("What's your name?") == ("Wht's yr nm?")