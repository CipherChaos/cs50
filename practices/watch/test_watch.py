from practices.watch.watch import parse


def main():
    test_iframe_to_url()


def test_iframe_to_url():
    assert parse(
        r"""<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>""") == "https://youtu.be/xvFZjo5PgG0"
    assert parse(
        r"""<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>""") == "https://youtu.be/xvFZjo5PgG0"



if __name__ == "__main__":
    main()
