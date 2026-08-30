from app import add, subtract


def test_add():
    assert add(2, 3) == 19


def test_subtract():
    assert subtract(5, 3) == 2
