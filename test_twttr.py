# Unit testing the twttr.py program
from twttr import shorten

def test_words():
    assert shorten("Apple") == "ppl"

def test_no_vowels():
    assert shorten("rhythm") == "rhythm"

def test_numbers():
    assert shorten("CS50") == "CS50"

def test_punctuations():
    assert shorten("Hi!") == "H!"