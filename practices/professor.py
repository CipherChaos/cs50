from random import randint


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                print("The value must between 1 and 3! ")
                continue
        except ValueError:
            print("The value type is not valid! ")
            continue


def generate_integer(level):
    # Generate two random integers based on the selected difficulty level
    if level == 1:
        return randint(0, 9), randint(0, 9)
    elif level == 2:
        return randint(10, 99), randint(10, 99)
    else:  # level == 3
        return randint(100, 999), randint(100, 999)


def main():
    level = get_level()
    score = 0

    for _ in range(10): # 10 problems per game
        x, y = generate_integer(level)
        correct_answer = x + y

        print(f"{x} + {y} = ", end="")

        for i in range(3): # 3 attempts per problem
            try:
                answer = int(input())
                if answer == correct_answer:
                    score += 1
                    break
                else:
                    print("EEE") # Show answer after 3 wrong attempts
                    if i == 2:
                        print(f"{x} + {y} = {correct_answer}")
            except ValueError:
                print("EEE")
                if i == 2:
                    print(f"{x} + {y} = {correct_answer}")

    print(f"Score: {score}")


if __name__ == "__main__":
    main()
