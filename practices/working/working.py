import re


def main():
    print(convert(input("Hours: ")))


def convert_hours(hh, mm, ss):
    hours = int(hh)
    if ss == "PM":

        if hours == 12:
            hh_update = 12
        else:
            hh_update = hours + 12
    else:
        if hours == 12:
            hh_update = 0
        else:
            hh_update = hours

    updated_time = f"{hh_update:02}" + ":" + f"{mm:02}"
    return updated_time


def convert(s):
    time_pattern = r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$"
    match = re.search(time_pattern, s, re.I)

    if match:
        time = list(match.groups())

        if time[1] is None:
            time[1] = 0

        if time[4] is None:
            time[4] = 0
        if int(time[0]) > 12 or int(time[3]) > 12:
            raise ValueError
        if int(time[1]) > 59 or int(time[4]) > 59:
            raise ValueError

        left_clock = convert_hours(time[0], time[1], time[2])
        right_clock = convert_hours(time[3], time[4], time[5])

        return left_clock + " to " + right_clock
    else:
        raise ValueError


if __name__ == "__main__":
    main()
