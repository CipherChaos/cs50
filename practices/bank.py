def value(greeting):

    greeting = greeting.lower().strip()

    if "hello" in greeting:
        amount = 0

    elif "hello" not in greeting and greeting.startswith('h'):
        amount = 20

    else:
        amount = 100

    return amount


def main():
    sample = input("Greeting: ")
    amount = value(sample)
    print(f"${amount}")


if __name__ == "__main__":
    main()
