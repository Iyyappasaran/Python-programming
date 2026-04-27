# Unit testing the bank.py program
from bank import value

def test_startsWith_hello():
    assert value("Hello, world") == 0

def test_startsWith_h():
    assert value("Hi, bro") == 20

def test_startsWith_neither():
    assert value("Good morning") == 100

def test_spaces():
    assert value("  Hello   ") == 0