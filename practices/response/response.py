from validator_collection import validators, checkers, errors


def main():
    email_validation()

def email_validation():
    email_add = input("What's your email address? ")

    print("Valid" if checkers.is_email(email_add) == True else "Invalid")


if __name__ == "__main__":
    main()
