import sys
import random
import pyfiglet


def main():
    # Initialize a Figlet object for text rendering
    figlet = pyfiglet.Figlet()

    # Check command-line arguments for font selectio
    if len(sys.argv) == 3:
        # If the user specifies a font with -f or --font
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            try:
                # Attempt to set the specified font
                figlet.setFont(font=sys.argv[2])
            except pyfiglet.FontNotFound:
                # Exit if the font doesn't exist
                sys.exit("Invalid usage")
        else:
            sys.exit("Invalid usage")
    # If no arguments, pick a random font
    elif len(sys.argv) == 1:
        fonts = figlet.getFonts()
        random_font = random.choice(fonts)
        figlet.setFont(font=random_font)
    # Exit if arguments are invalid (e.g., wrong number of args)
    else:
        sys.exit("Invalid usage")

    # Get user input and render it in the selected font
    text = input("Input: ")
    print(f"Output: \n {figlet.renderText(text)}")


if __name__ == "__main__":
    main()
