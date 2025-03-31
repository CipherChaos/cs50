def convert(fraction):
    num, den = map(int, fraction.split("/"))

    if den == 0:
        raise ZeroDivisionError
    if num > den:
        raise ValueError

    return round((num / den) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    return f"{percentage}%"


def main():
    while True:
        try:
            fraction = input("Fraction: ").strip()
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except ValueError:
            print("Invalid input. Please enter as X/Y.")
        except ZeroDivisionError:
            print("Denominator cannot be zero. Try again.")


if __name__ == "__main__":
    main()
