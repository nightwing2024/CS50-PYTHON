from bank import value


def test_first():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("    Hello") == 0


def test_second():
    assert value("Hey") == 20
    assert value("Hallo") == 20
    assert value("    Hallo") == 20


def test_third():
    assert value("") == 100
    assert value("OtherName") == 100
    assert value("  AnotherName") == 100
