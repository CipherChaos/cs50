

while True:
    try:
        sample = input("Fraction: ").strip().split(
            "/")

        var1 = int(sample[0])
        var2 = int(sample[1])

        if len(sample) != 2 or var1 > var2:
            raise ValueError

        if var2 == 0:
            raise ZeroDivisionError

        calculus = (var1 / var2) * 100

        if calculus <= 1:
            print("E")
        elif calculus >= 99:
            print("F")
        else:
            print(f"{round(calculus)}%")
        break

    except ValueError:
        print("Invalid input. Please enter as X/Y.")
    except ZeroDivisionError:
        print("Denominator cannot be zero. Try again.")
