import re


def extract_number(raw_string):
    return float(next(iter(re.findall(r"[0-9]+", raw_string)), 0))


def tip(dollars, percent):

    percent_to_float = extract_number(dollars)
    dollars_to_float = extract_number(percent)

    total_tip = dollars_to_float * percent_to_float / 100
    print(f"Leave ${total_tip:.2f}")


def main():

    dollars = input("How much was the meal? ")
    percent = input("What percentage would you like to tip? ")
    tip(dollars, percent)


if __name__ == "__main__":
    main()
