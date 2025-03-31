import sys
import csv


def main():
    argument_count = len(sys.argv)

    if argument_count < 3:
        sys.exit("Too few command-line arguments")
    if argument_count > 3:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".csv") and sys.argv[2].endswith("csv"):
        sys.exit("Not a Python file")
    try:
        with open(sys.argv[1], 'r') as file:
            lines = csv.DictReader(file)
            students = list(lines)

    except FileNotFoundError:
        sys.exit(f"File does not exist")

    else:
        new_students = []
        for row in students:
            last, first = row["name"].split(", ")
            new_students.append(
                {"first": first, "last": last, "house": row["house"]})

        names_subject = ["first", "last", "house"]
        with open(sys.argv[2], 'w', newline="") as file:
            writer = csv.DictWriter(file, fieldnames=names_subject)
            writer.writeheader()
            writer.writerows(new_students)


if __name__ == "__main__":
    main()
