from practices.plates import is_valid

def test_cs50():
    assert is_valid("CS50") == "Valid"
    assert is_valid("CS05") == "Invalid"
    assert is_valid("CS50P2") == "Invalid"


def test_characters():
    assert is_valid("H") == "Invalid"


def test_numbers():
    assert is_valid("50") == "Invalid"
    assert is_valid("PI3.14") == "Invalid"


def test_others():
    assert is_valid("OUTATIME") == "Invalid"
    assert is_valid("ECTO88") == "Valid"
    assert is_valid("NRVOUS") == "Valid"


def main():
    test_cs50()
    test_characters()
    test_numbers()
    test_others()


if __name__ == "__main__":
    main()
