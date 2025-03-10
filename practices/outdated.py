import re

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

sample = input().strip().title()

res = re.split(r"[,/ ]+", sample)

print(*res[::-1], sep='-')
