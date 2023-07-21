import sys
from pyfiglet import Figlet
import random


figlet = Figlet()
fonts = figlet.getFonts()

if  len(sys.argv) < 2:
    f = random.choice(fonts)
    figlet.setFont(font=f)
    print(figlet.renderText(s))
elif len(sys.argv) > 2:
    if (sys.argv[1] == '-f'  or sys.argv[1] == '--font'):
        if sys.argv[2] in fonts:
            f = sys.argv[2]
            figlet.setFont(font=f)
            s = input("Input: ")
            print(figlet.renderText(s))
        else:
            print("Invalid Usage")
            sys.exit(1)
    else:
        print("Invalid Usage")
        sys.exit(1)

else:
    print("Invalid Usage")
    sys.exit(1)









