import sys
import random
from pyfiglet import Figlet


def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    try:
        if len(sys.argv) == 1:
            str = input("Input: ")
            f = random.choice(figlet.getFonts())
            figlet.setFont(font=f)
            print(f"Output: {figlet.renderText(str)}")

        elif sys.argv[1] =='-f' or sys.argv[1] =="--font":
            if sys.argv[2] in figlet.getFonts():
                str = input("Input: ")
                figlet.setFont(font=sys.argv[2])
                print(f"Output:{figlet.renderText(str)}")
            else:
                sys.exit('Invalid usage')
        else:
            sys.exit('Invalid usage')
    except:
        sys.exit('Invalid usage')

main()
