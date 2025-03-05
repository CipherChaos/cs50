vowels = {'a', 'e', 'i', 'o', 'u'}

sample = input("Input: ")

output = "".join(char for char in sample if char.lower() not in vowels)

print(f"Output: {output}")
