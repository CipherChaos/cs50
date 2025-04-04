import pytest
from practices.validate.numb3rs import validate

def main():
    test_ip()
    test_ip_range()

def test_ip():
    assert validate("10.20.30.40") == False
    assert validate("10.20.30") == False
    assert validate("10.20") == False
    assert validate("10") == False

def test_ip_range():
    assert validate(r"127.0.0.1") == True
    assert validate(r"255.255.255.255") == True
    assert validate(r"512.512.512.512") == False
    assert validate(r"256.1.1.1") == False
    assert validate(r"cat") == False


if __name__ == "__main__":
    main()