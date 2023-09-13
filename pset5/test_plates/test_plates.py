from plates import is_valid

def test_valid():
    assert is_valid("CS50") == True


def test_zero_first():
    assert is_valid("CS05") == False


def test_digit_middle():
    assert is_valid("CS50P") == False


def test_invalid_symbols():
    assert is_valid("PI3.14") == False


def test_max_min():
    assert is_valid("OUTATIME") == False
    assert is_valid("H") == False

def test_digit_beginning():
    assert is_valid("10CCA3") == False


def test_all_digit():
    assert is_valid("123456") == False
