foods_dict = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

while True:
    try:
        sample = input("Item: ").title()

        if sample in foods_dict:
            total += foods_dict[sample]
            print(f"Total: ${total:.2f}")
        else:
            continue

    except EOFError:
        print(f"\nTotal: ${total:.2f}")
        break
