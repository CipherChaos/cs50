import pytest
from .seasons import check_birth_date, calculate_distance
from datetime import date


def test_check_birth_date():
    assert check_birth_date(2024, 4, 11) == date(2024, 4, 11)
    assert check_birth_date(2024, 31, 10) == "Invalid Date"

def test_calculate_distance():
    assert calculate_distance(date(2024, 4, 11)) == 525600

def main():
    test_check_birth_date()

if __name__ == "__main__":
    main()