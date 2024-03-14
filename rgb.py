import curtsies
from curtsies.fmtfuncs import *

print('\033[?25l', end="")
print("----- Colour Picker -----")

colour = [0, 0, 0]
selected = 0

cube = str(str("█" * 10) + "\n") * 5 

def print_content(clear=True):
    if clear:
        print('\033[8A')

    if selected == 0:
        print(f"RGB: |{underline(str(colour[0]))}|{colour[1]}|{colour[2]}|")
    elif selected == 1:
        print(f"RGB: |{colour[0]}|{underline(str(colour[1]))}|{colour[2]}|")
    elif selected == 2:
        print(f"RGB: |{colour[0]}|{colour[1]}|{underline(str(colour[2]))}|")
    
    print(f"\033[38;2;{colour[0]};{colour[1]};{colour[2]}m" + cube + "\033[0m")

# from time import sleep
# 
# print("rgb: 0,0,0")
# print("HERE IS THE COLOUR")
# sleep(1)
# print('\033[3A')
# print("rgb: 1,1,1")
# print("HERE IS THE NEW COLOUR")


    
print_content(clear=False)   

with curtsies.Input(keynames="curtsies") as input_generator:
    for e in curtsies.Input():
        if e in ("<ESC>", "<Ctrl-d>", "q"):
            break
        if e == "<UP>" or e == "k":
           colour[selected] += 1
           if colour[selected] > 255:
               colour[selected] = 255 
           print_content()
        elif e == "<DOWN>" or e == "j":
            colour[selected] -= 1
            if colour[selected] < 0:
                colour[selected] = 0
            print_content()
        elif e == "<LEFT>" or e == "h":
            selected -= 1
            if selected < 0:
                selected = 0
            print_content()
        elif e == "<RIGHT>" or e == "l":
            selected += 1
            if selected > 2:
                selected = 2
            print_content()

