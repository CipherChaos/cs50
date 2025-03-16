from random import randint

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                if level == 1:
                    return [0, 9]
                elif level == 2:
                    return [10, 99]
                elif level == 3:
                    return [100, 999]
                else:
                    print("The number should be less than 4!")
            else:
                print("Please enter a positive number!")
        except ValueError:
            print("Value type is not Valid!")

def user_answer():
    while True:
        try:
            answer = int(input(""))
            return answer
        except ValueError:
            print("Value type is not Valid!")

def generate_integer(level):

    x = randint(level[0], level[1])
    y = randint(level[0], level[1])
    equation = x + y
    return x, y, equation

def main():
    level = get_level()
    score = 0
    for _ in range(10):
        attempts = 0
        correct = False
        x, y, equation = generate_integer(level)
        print(f"{x} + {y} = ", end="")


        while attempts < 3:
            user_response = user_answer()
            if user_response == equation:
                score += 1
                correct = True
                break
            else:
                attempts += 1
                print("EEE")

        if not correct:
            print(f"The correct answer was {equation}.")

    print(f"Your final score is: {score}")

if __name__ == "__main__":
    main()
