from practices.twttr import shorten


def test_twttr():
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"
    assert shorten("PYTHON") == "PYTHN"

def main():
    test_twttr()


if __name__ == "__main__":
    main()
