from working import convert
import pytest

def test_wrong_format():
    with pytest.raises(ValueError):
        convert("9 BM to 12 CM")
    with pytest.raises(ValueError):
        convert("9 AM - 12 PM")

def test_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"


def test_wrong_hour():
    with pytest.raises(ValueError):
        convert("9 AM to 42 PM")

def test_wrong_minute():
    with pytest.raises(ValueError):
        convert("9:72 AM to 12:80 PM")