# Unit testing working.py program
from working import convert
from pytest import raises

def test_default():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
def test_default2():
    assert convert("9 AM to 4 PM") == "09:00 to 16:00"
def test_default3():
    assert convert("9 AM to 3:00 PM") == "09:00 to 15:00"
def test_default4():
    assert convert("9:00 AM to 6 PM") == "09:00 to 18:00"
def test_error():
    with raises(ValueError):
        convert("9:00 AM to 5:00PM")
def test_error2():
    with raises(ValueError):
        convert("9:60 AM to 5:00 PM")
def test_error3():
    with raises(ValueError):
        convert("9:00 AM to 13:00 PM")