import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time_pattern = r"^(\d{1,2}:?\d{2})? (A|P\M) to$"
    match = re.search(time_pattern, s)
    if match:
        return match.group()
    else:
        return None

    """
    
        9 AM to 5 PM
        9:00 AM to 5:00 PM
        10 AM to 8:50 PM
        10:30 PM to 8 AM
        9 AM to 5 PM
    
    """


if __name__ == "__main__":
    main()
