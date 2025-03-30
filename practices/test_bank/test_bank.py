from practices.bank import value


def test_hello():
    assert value("Hello") == 0
    assert value(" Hello ") == 0


def test_startwith_h():
    assert value("Hello, Newman") == 0
    assert value("How you doing?") == 20


def test_others():
    assert value("What's happening?") == 100
    assert value("What's up?") == 100


def main():
    test_hello()
    test_startwith_h()
    test_others()


if __name__ == "__main__":
    main()
