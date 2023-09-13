from bank import value


def test_startswith_hello():
    assert value("Hello") == 0


def test_startswith_h():
    assert value("How you doing?") == 20


def test_startswith_other():
    assert value("What's happening?") == 100