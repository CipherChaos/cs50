def main():
    plate = input("Plate: ")

    valkeys = ["ECTO88", "CS50", "NRVOUS"]

    if plate in valkeys:
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
