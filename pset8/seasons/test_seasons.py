from seasons import calculate

def test_valid_date():
    assert calculate("2000-09-16") == "Twelve million, ninety thousand, two hundred forty minutes"

def test_invalid_date():
    assert calculate("2024-13-53") == "Invalid date"
