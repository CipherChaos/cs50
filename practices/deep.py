user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower(
).strip().replace(" ", "-")

if user_input in ["forty-two", "42"]:
    print("yes")

else:
    print("no")
