import pytest
from practices.um.um import count

def test_count():
    assert count("hello, um, world") == 1
    assert count("um, hello, um, world") == 2
    assert count("um...") == 1
    assert count("um?") == 1
    assert count("um") == 1

def test_format_check():
    assert count("yum") == 0
    assert count("yummy") == 0
    assert count("album") == 0

def test_case_insensitivity():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2


def main():

    test_count()
    test_format_check()
    test_case_insensitivity()

if __name__ == "__main__":
    main()

