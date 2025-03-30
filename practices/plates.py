def is_valid(string):
    valkeys = ["ECTO88", "CS50", "NRVOUS"]

    if string in valkeys:
        return "Valid"
    else:
        return "Invalid"


def main():
    plate = input("Plate: ")
    validation_answer_check = is_valid(plate)
    print(validation_answer_check)


if __name__ == "__main__":
    main()
