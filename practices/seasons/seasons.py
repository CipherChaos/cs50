from datetime import date
import sys
import inflect


p = inflect.engine()

def check_birth_date(year,month,day):
    try:
        time = date(year, month, day)
    except ValueError:
        return "Invalid Date"
    return time

def calculate_distance(time):
    today_date = (date.today() - time).days
    return str(today_date * 24 * 60)

def main():
    try:
        year, month, day = [int(_) for _ in input("Date of Birth:").split("-")]
    except ValueError:
       sys.exit("Invalid Date")

    time = check_birth_date(year,month,day)
    distance_minutes = calculate_distance(time)
    words = p.number_to_words(distance_minutes, andword="")
    print(words.capitalize() + " minutes")


if __name__ == "__main__":
    main()


