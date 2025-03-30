def main():
    sample = input("Input: ")
    print(shorten(sample))


def shorten(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    output = "".join(char for char in word if char.lower() not in vowels)

    return output


if __name__ == "__main__":
    main()
