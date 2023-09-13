from numb3rs import validate

def test_out_of_range():
    assert validate("256.256.256.256") == False
    assert validate("-1.-1.-1.-1") == False
    assert validate("64.128.256.512") == False

def test_non_numeric():
    assert validate("cat") == False

def test_valid():
    assert validate("192.168.254.254") == True
    assert validate("255.255.255.255") == True