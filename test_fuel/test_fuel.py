import pytest
from fuel import convert, gauge


def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("Cat/Dog")


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(25) == "25%"


def test_fraction():
    assert convert("1/4") == 25
    assert convert ("1/100") == 1
    assert convert ("99/100") == 99
