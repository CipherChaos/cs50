import sys
import csv
from tabulate import tabulate


def read_file(filename):
    with open(filename, 'r') as file:
        lines = csv.reader(file)
        menu = list(lines)
    return menu


def main():
    argument_count = len(sys.argv)

    if argument_count < 2:
        sys.exit("Too few command-line arguments")
    if argument_count > 2:
        sys.exit("Too many command-line arguments")

    target_file = sys.argv[1]

    if not target_file.endswith(".csv"):
        sys.exit("Not a CSB file")
    try:
        menu = read_file(target_file)
    except FileNotFoundError:
        sys.exit(f"File does not exist")
    else:
        print(tabulate(menu, headers="firstrow", tablefmt="grid"))


if __name__ == "__main__":
    main()
