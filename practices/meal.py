def frange(start, stop, step):
    while start < stop:
        yield round(start, 10)
        start += step


sample = float(input("What time is it?: "))


if sample in frange(6, 12, 0.01):
    print("breakfast time")
elif sample in frange(12, 17, 0.01):
    print("lunch time")
elif sample in frange(17, 22, 0.01):
    print("dinner time")
