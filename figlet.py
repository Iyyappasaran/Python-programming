# Prompts the user for a str of text and outputs the text in the desired font
import sys
from pyfiglet import Figlet
import random

def main():
    figlet = Figlet()
    if len(sys.argv) == 1:
        font = random.choice(figlet.getFonts())
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
        font = sys.argv[2]
        if font not in figlet.getFonts():
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
    
    figlet.setFont(font=font)
    text = input("Input: ")
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
    