import pytest
from working import convert

def test_valid_input_am_to_am():
    assert convert("9:30 AM to 11:45 AM") == "09:30 to 11:45"

def test_valid_input_am_to_pm():
    assert convert("10:00 AM to 1:30 PM") == "10:00 to 13:30"

def test_valid_input_pm_to_pm():
    assert convert("5:15 PM to 8:00 PM") == "17:15 to 20:00"

def test_valid_input_pm_to_am():
    assert convert("9:00 PM to 3:45 AM") == "21:00 to 03:45"

def test_valid_input_hour_without_minutes_am_to_pm():
    assert convert("9 AM to 1 PM") == "09:00 to 13:00"

def test_valid_input_hour_without_minutes_pm_to_am():
    assert convert("9 PM to 3 AM") == "21:00 to 03:00"

def test_valid_input_hour_with_single_digit_hour_am_to_pm():
    assert convert("9:00 AM to 1:30 PM") == "09:00 to 13:30"

def test_valid_input_hour_with_single_digit_hour_pm_to_am():
    assert convert("9:00 PM to 3:45 AM") == "21:00 to 03:45"

def test_valid_input_hour_with_missing_start_minutes_am_to_pm():
    assert convert("9 AM to 1:30 PM") == "09:00 to 13:30"

def test_valid_input_hour_with_missing_start_minutes_pm_to_am():
    assert convert("9 PM to 3:45 AM") == "21:00 to 03:45"

def test_invalid_hour_format():
    with pytest.raises(ValueError):
        convert("13:30 AM to 3:45 PM")

def test_invalid_minute_format():
    with pytest.raises(ValueError):
        convert("9:70 AM to 11:20 AM")

def test_invalid_period_format():
    with pytest.raises(ValueError):
        convert("9:30 LM to 11:45 PM")

def test_invalid_input_format():
    with pytest.raises(ValueError):
        convert("Invalid input")

if __name__ == "__main__":
    pytest.main()
