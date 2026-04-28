# Unit testing the plates.py program
from plates import is_valid

def test_lettersOnly():
    assert is_valid("HELLO")

def test_start():
    assert is_valid("AA55")
    assert not is_valid("A55")

def test_limit():
    assert is_valid("AAA222")
    assert not is_valid("AAAA2222")

def test_number():
    assert is_valid("AA200")
    assert not is_valid("AA22A")

def test_zero():
    assert not is_valid("AA02")

def test_special():
    assert is_valid("AA30")
    assert not is_valid(" AA30")