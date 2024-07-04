import pytest
from numb3rs import validate

def test_numbers1():
    assert validate(r"127.0.0.1") == True
    assert validate (r"255.255.234") == False
    assert validate (r"512.512") == False
    assert validate (r"1.2") == False

def test_numbers2():
    assert validate (r"255.255.255.255") == True
    assert validate (r"512.1.1.1") == False
    assert validate (r"1.512.1.1") == False
    assert validate (r"1.1.512.1") == False
    assert validate (r"1.1.1.512") == False


def test_letters():
    assert validate ("cat") == False
    assert validate ("dog") == False
