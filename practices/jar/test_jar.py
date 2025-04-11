import pytest
from jar import Jar


def test_init():
    # Test default initialization
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    # Test custom capacity
    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.size == 0

    # Test negative capacity
    with pytest.raises(ValueError):
        jar = Jar(-1)

    # Test non-integer capacity
    with pytest.raises(TypeError):
        jar = Jar("invalid")


def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪"

    jar.withdraw(1)
    assert str(jar) == "🍪🍪"


def test_deposit():
    jar = Jar(10)

    # Test valid deposits
    jar.deposit(5)
    assert jar.size == 5

    jar.deposit(3)
    assert jar.size == 8

    # Test depositing 0 cookies
    jar.deposit(0)
    assert jar.size == 8

    # Test depositing more than capacity
    with pytest.raises(ValueError):
        jar.deposit(3)

    # Test depositing a negative number
    with pytest.raises(ValueError):
        jar.deposit(-1)

    # Make sure the jar size didn't change after failed deposits
    assert jar.size == 8


def test_withdraw():
    jar = Jar(10)
    jar.deposit(8)

    # Test valid withdrawals
    jar.withdraw(3)
    assert jar.size == 5

    jar.withdraw(2)
    assert jar.size == 3

    # Test withdrawing 0 cookies
    jar.withdraw(0)
    assert jar.size == 3

    # Test withdrawing more than available
    with pytest.raises(ValueError):
        jar.withdraw(4)

    # Test withdrawing a negative number
    with pytest.raises(ValueError):
        jar.withdraw(-1)

    # Make sure the jar size didn't change after failed withdrawals
    assert jar.size == 3

    # Test withdrawing all remaining cookies
    jar.withdraw(3)
    assert jar.size == 0


def test_capacity_property():
    jar = Jar(10)

    # Test that capacity property works correctly
    assert jar.capacity == 10

    # Test changing capacity
    with pytest.raises(AttributeError):
        jar.capacity = 15  # capacity should be read-only after initialization


def test_size_property():
    jar = Jar(10)

    # Test initial size
    assert jar.size == 0

    # Test size after deposit
    jar.deposit(5)
    assert jar.size == 5

    # Test setting size directly
    jar.size = 3
    assert jar.size == 3

    # Test setting invalid size
    with pytest.raises(ValueError):
        jar.size = -1

    with pytest.raises(ValueError):
        jar.size = 11  # Exceeds capacity

    with pytest.raises(TypeError):
        jar.size = "invalid"