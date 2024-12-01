"""
|| शुभ लाभ ||

Resistor Color Coding Program for 4 band(v1.0):
1. Enter 4 band colors
2. Receive resistor value
"""

from easygui import *
def ColorCode():
    # Initializing easygui details
    text = ""
    image = "4resistor.jpg"
    title = "Resistor Color Coding"
    button_list_3 = ["black", "brown", "red", "orange", "yellow", "green", "blue",
                     "violet", "grey", "white"]
    button_list_tole = ["gold", "silver", "none"]
    color_details = []
    button_list_1 = ["brown", "red", "orange", "yellow", "green", "blue",
                     "violet", "grey", "white"]

    text = "Choose band 1 color"
    tempcolor = buttonbox(text, title,  choices = button_list_1) # For first band
    color_details.append(tempcolor)

    for col in range(1,4): # For last 3 bands
        text = "Choose band " + str((col+1)) + " color"
        if col != 3 : # For first 3 bands
            tempcolor = buttonbox(text, title,  choices = button_list_3)
        else :
            tempcolor = buttonbox(text, title, choices = button_list_tole)

        color_details.append(tempcolor) # Append clicked colors

    return color_details

def Display(res_colors, first_three, tolerance):

    res = first_three
    #If blocks for large resistance values
    if res >= 1000000.0: # If value is in mega ohms
        res = str(res/1000000.0) + " M"
    elif res >= 1000.0: # If value is in kilo ohms
        res = str(res/1000.0) + " K"

    #If blocks for tolerance band
    if res_colors[3] == "gold":
        res = str(res) + "Ω ± " + tolerance[0]
    elif res_colors[3] == "silver":
        res = str(res) + "Ω ± " + tolerance[1]
    else:
        res = str(res) + " Ω ± " + tolerance[2]

    message = "Resistance = " + str(res)
    title = "Result"
    ok_btn_txt = "Thanks :)"
    msgbox(message, title, ok_btn_txt)


# Main Program :
# array declarations
colors = ["black", "brown", "red", "orange", "yellow", "green", "blue",
          "violet", "grey", "white", "gold", "silver", "none"]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
multiplier = [0.1, 0.01]
tolerance = ["5%", "10%", "20%"]

text = "Refer to colors : "
title = "Resistor color coding"
img = "colorcoding.jpg"
button_list = ["Continue"]
buttonbox(text, title, image = img, choices = button_list)

res_colors = ColorCode() # Calling function to get visual input
first_two = str(colors.index(res_colors[0])) + str(colors.index(res_colors[1]))
first_three = int(first_two) * (10 ** (colors.index(res_colors[2])))

Display(res_colors, first_three, tolerance) #Calling final function
