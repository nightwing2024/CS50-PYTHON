import pytest
from twttr import shorten


def main():
    test_twtter()


def test_twtter():
    assert shorten("Hola") == "Hl"
    assert shorten("1") == "1"
    assert shorten("!!!") == "!!!"

def test_upper():
    assert shorten("HOLA") == "HL"

def punctuation():
    assert shorten("Hola,Mnd") == "Hl,Mnd"
