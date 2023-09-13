from um import count

def test_count():
    assert count("um, um, um") == 3

def test_um_sentence():
    assert count("um, Thanks for the album") == 1

def test_um_uppercase():
    assert count("Um, Thanks um, for the um, album") == 3