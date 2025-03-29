import re


def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    sample = input().strip().title()

    res = re.split(r"[,/ ]+", sample)

    print(*res[::-1], sep='-')


if __name__ == "__main__":
    main()
