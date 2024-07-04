from plates import is_valid

#  vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
def test_characters():
    assert is_valid("HH") == True
    assert is_valid("H") == False
    assert is_valid("HHHHHH") == True
    assert is_valid("HHHHHHH") == False

# All vanity plates must start with at least two letters
def test_start():
    assert is_valid("AA") == True
    assert is_valid ("A1") == False
    assert is_valid("01") == False
    assert is_valid("1A") == False
## Numbers cannot be used in the middle of a plate;
#they must come at the end. For example, AAA222 would be an acceptable … vanity plate;
#AAA22A would not be acceptable. The first number used cannot be a ‘0’.”

def test_middle():
    assert is_valid("AAA222") == True
    assert is_valid("CS50P2") == False
    assert is_valid("CS05P2") == False
    assert is_valid("CS0002") == False


# No periods, spaces, or punctuation marks are allowed

def test_punctuation():
    assert is_valid("PI3.14") == False
