import sys
import random
from pyfiglet import Figlet
figlet = Figlet()
if len(sys.argv) == 1:
    #Getting an input from the user
    x = input("Input: ")
    #Getting a list of all possible fonts
    fonts = figlet.getFonts()
    #Selecting a random font
    choosen_font = random.choice(fonts)
    figlet.setFont(font=choosen_font)
    print(figlet.renderText(x))
elif len(sys.argv) == 3:
    #Getting an input from the user
    y = input("Input: ")
    #Getting the specified font from the command line argument
    font_choosen = sys.argv[2]
    fonts = figlet.getFonts()
    if font_choosen in fonts and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        figlet.setFont(font=font_choosen)
        print(figlet.renderText(y))
    else:
        sys.exit()
else:
    sys.exit()

