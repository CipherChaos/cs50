import sys


def main():
    argument_count = len(sys.argv)

    if argument_count < 2:
        sys.exit("Too few command-line arguments")
    if argument_count > 2:
        sys.exit("Too many command-line arguments")

    target_file = sys.argv[1]

    if not target_file.endswith(".py"):
        sys.exit("Not a Python file")
    try:
        with open(target_file, 'r') as file:
            lines = file.readlines()

    except FileNotFoundError:
        sys.exit(f"File does not exist")
    else:
        lines_count = 0
        for line in lines:
            stripped_lines = line.strip()
            if stripped_lines == '' or stripped_lines.startswith('#'):
                continue
            lines_count += 1

    print(lines_count)

if __name__ == "__main__":
    main()
