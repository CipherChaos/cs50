sample = input("Greeting: ").lower()
print(sample)

if "hello" not in sample and sample.startswith('h'):
    print("$20")

elif "hello" in sample:
    print("$0")

else:
    print("$100")
