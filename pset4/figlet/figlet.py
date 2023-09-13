import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    fonts = ['small','starwars','stop','straight','standard']

    if len(sys.argv) == 1:
        figlet.getFonts()
        figlet.setFont(font=random.choice(fonts))

        str = input("Input: ")
        print(figlet.renderText(str))

    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        figlet.getFonts()

        try:
            figlet.setFont(font=sys.argv[2])
        except:
            sys.exit("Font Not Found")

        str = input("Input: ")
        print(figlet.renderText(str))

    else:
        sys.exit("Invalid usage")

if __name__ == "__main__":
    main()