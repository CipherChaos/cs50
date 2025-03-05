amount_due = 50
valid_coins = [5, 10, 25]

while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    insert_coin = int(input("Insert Coin: "))

    if insert_coin in valid_coins:
        amount_due -= insert_coin

print(f"Change Owed: {abs(amount_due)}")
