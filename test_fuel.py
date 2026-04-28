# Unit testing fuel.py program
from fuel import convert
from fuel import gauge
from pytest import raises

def test_fuel():
    assert convert("1/4") == 25

def test_lessFuel():
    assert gauge(1) == "E"

def test_moreFuel():
    assert gauge(99) == "F"

def test_gauge():
    assert gauge(50) == "50%"

def test_ValueError():
    with raises(ValueError):
        convert("2/1")

def test_ZeroDivisionError():
    with raises(ZeroDivisionError):
        convert("2/0")