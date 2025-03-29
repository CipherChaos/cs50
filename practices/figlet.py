import sys
import random
import pyfiglet


def main():
    figlet = pyfiglet.Figlet()

    if len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            try:
                figlet.setFont(font=sys.argv[2])
            except pyfiglet.FontNotFound:
                sys.exit("Invalid usage")
        else:
            sys.exit("Invalid usage")

    elif len(sys.argv) == 1:
        fonts = figlet.getFonts()
        random_font = random.choice(fonts)
        figlet.setFont(font=random_font)
    else:
        sys.exit("Invalid usage")

    text = input("Input: ")
    print(f"Output: \n {figlet.renderText(text)}")


if __name__ == "__main__":
    main()
