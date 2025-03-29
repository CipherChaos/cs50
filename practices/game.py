from random import randint


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_guess():
    while True:
        try:
            guess = int(input("Guess: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    level = get_level()
    answer = randint(1, level)

    while True:
        user_answer = get_guess()

        if user_answer < 1 or user_answer > level:
            print("Too large!")
            continue

        if user_answer < answer:
            print("Too small!")
        elif user_answer > answer:
            print("Too large!")
        else:
            print("Just right!")
            break


if __name__ == "__main__":
    main()
