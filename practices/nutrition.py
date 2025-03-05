facts = {"apple": 130, "Avocado": 50,
         "Sweet Cherries": 100, "pear": 100, "Kiwifruit": 90}

sample = input("Item: ")

if sample in facts:
    print("Callories:", facts[sample])
