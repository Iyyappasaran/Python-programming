# Unit testing numb3rs.py file

from numb3rs import validate

def test_default():
    assert validate("12.13.14.15")

def test_validate():
    assert not validate("12.16.288.19")

def test_non_integers():
    assert not validate("a.12.15.100")

def test_special_case():
    assert validate("001.003.002.078")