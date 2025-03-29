import re


def convert_case(s):
    if "_" in s:
        parts = s.split("_")
        return parts[0] + "".join(word.capitalize() for word in parts[1:])
    else:

        return re.sub(r'([a-z])([A-Z])', r'\1_\2', s).lower()


def main():
    user_input = input("Enter a string in camelCase or snake_case: ")
    converted = convert_case(user_input)
    print("Converted:", converted)


if __name__ == "__main__":
    main()
