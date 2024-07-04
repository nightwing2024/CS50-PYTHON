import pytest
from um import count

# Test case for empty text
def test_count_empty_text():
    assert count("") == 0

# Test case for text with no occurrences of the word
def test_count_no_occurrences():
    assert count("This is a text without the searched word.") == 0

# Test case for exact occurrence of the word
def test_count_one_exact_occurrence():
    assert count("The searched word is 'um'.") == 1

# Test case for multiple occurrences of the word (case insensitive)
def test_count_multiple_occurrences():
    assert count("Um UM um uM UMUmUM") == 4

# Test case for partial occurrences (part of another word)
def test_count_partial_occurrences():
    assert count("The result will be to sum the numbers.") == 0

# Test case for occurrences with special characters around
def test_count_special_characters_around():
    assert count("This is an example: um, um. Does it work correctly?") == 2

# Test case for occurrences with special characters inside the word
def test_count_special_characters_inside():
    assert count("Example: 'u*m', 'UM', 'U.M'") == 1

# Test case for text with multiple words separated by spaces
def test_count_multiple_words():
    assert count("The sum of um, um, UM, UM and others is UM + um.") == 6

# Test case for words that are part of other words
def test_count_subword_occurrences():
    assert count("The light of the moon is beautiful.") == 0

# Test case for words that are part of other words with different capitalization
def test_count_subword_occurrences_case_insensitive():
    assert count("The light of the Moon is beautiful.") == 0
