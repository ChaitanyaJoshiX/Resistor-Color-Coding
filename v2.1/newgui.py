from customtkinter import *
from CTkMessagebox import *
from PIL import Image
import time
import sys

def Started():
    begin_button.place_forget()
    pic_frame.place_forget()
    bands_frame.place(relx=0.5, rely=0.5, anchor="center")
    band1_label.place(relx=0.5, rely=0.05, anchor="n")
    band1_buttons.place(relx=0.5, rely=0.65, anchor="s")

def Reset():
    user_bands.clear()
    band1_label.place_forget()
    band1_buttons.place_forget()
    band2_label.place_forget()
    band2_buttons.place_forget()
    band3_label.place_forget()
    band3_buttons.place_forget()
    band4_label.place_forget()
    band4_buttons.place_forget()
    Started()

def InitColValues(band_colors):
    i=0
    col_dict = dict()
    for color in band_colors[:10]:
        col_dict[color] = i
        i+=1
    return col_dict

def band1(value):
    user_bands.append(value)
    band1_label.place_forget()
    band1_buttons.place_forget()
    band2_label.place(relx=0.5, rely=0.05, anchor="n")
    band2_buttons.place(relx=0.5, rely=0.65, anchor="s")

def band2(value):
    user_bands.append(value)
    band2_label.place_forget()
    band2_buttons.place_forget()
    band3_label.place(relx=0.5, rely=0.05, anchor="n")
    band3_buttons.place(relx=0.5, rely=0.65, anchor="s")

def band3(value):
    user_bands.append(value)
    band3_label.place_forget()
    band3_buttons.place_forget()
    band4_label.place(relx=0.5, rely=0.05, anchor="n")
    band4_buttons.place(relx=0.5, rely=0.65, anchor="s")

def band4(value):
    user_bands.append(value)
    band4_label.place_forget()
    band4_buttons.place_forget()
    CalcRes(user_bands,band_dict, tol_dict)

def CalcRes(user_bands,band_dict, tol_dict):
    res = ""
    tempband = band_dict[user_bands[0]]
    res += str(tempband)
    tempband = band_dict[user_bands[1]]
    res += str(tempband)
    tempband = band_dict[user_bands[2]]
    res = float(res)*(10 ** (tempband))
    res = CorrectUnit(res)
    tempband = tol_dict[user_bands[3]]
    res += "Ω ± " + str(tempband)
    DisplayRes(res)

def CorrectUnit(res):
    if res >= 1000000000.0: # If value is in giga ohms
        res = str(res/1000000000.0)
        if res[-1:-3:-1] == "0.":
            res = res[0:-2]
        res += "G"

    elif res >= 1000000.0: # If value is in mega ohms
        res = str(res/1000000.0)
        if res[-1:-3:-1] == "0.":
            res = res[0:-2]
        res += "M"

    elif res >= 1000.0: # If value is in giga ohms
        res = str(res/1000.0)
        if res[-1:-3:-1] == "0.":
            res = res[0:-2]
        res += "K"

    else:
        res = str(res)
        if res[-1:-3:-1] == "0.":
            res = res[0:-2]

    return str(res)

def DisplayRes(res):
    title_label.place_forget()
    bands_frame.place_forget()
    final_message = CTkMessagebox(title="Result",icon="check",bg_color="transparent",fade_in_duration=1,message=res,option_1="End", option_2="Again",font=("Arial", 30, "bold"),width=500,height=300)
    if(final_message.get() == "Again"):
        Reset()
    else:
        sys.exit()


root = CTk()
root.title("Resistors")
root._state_before_windows_set_titlebar_color = 'zoomed'
set_appearance_mode("dark")
title_label = CTkLabel(root,text="Resistor's Color Coding",font=("Times New Roman", 50, "bold"),text_color="#d72631")
title_label.place(relx=0.5,rely=0.05,anchor=N)

pic_frame = CTkFrame(root,width=910,height=610,fg_color="transparent",border_width=200,border_color="#5c3c92")
pic_frame.place(relx=0.5, rely=0.5, anchor="center")

color_code = CTkImage(light_image=Image.open("colorcode.png"),size=(900,600))
image_label = CTkLabel(pic_frame,text="",image=color_code)
image_label.place(relx=0.5, rely=0.5, anchor="center")

begin_button = CTkButton(root,text="Begin",command=Started,width=200,height=80,border_width=5,fg_color="#077b8a",border_color="#a2d5c6",font=("Times New Roman", 20),text_color="black")
begin_button.place(relx=0.5,rely=0.82,anchor=N)

bands_frame = CTkFrame(root,width=800,height=600,fg_color="transparent",border_width=5,border_color="#5c3c92")
band_colors = ['Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue',
                'Violet', 'Grey', 'White', 'Gold', 'Silver', 'None']
band_dict = InitColValues(band_colors[:10])
tol_dict = {'Gold':"5%", 'Silver':"10%", 'None':"20%"}
user_bands = list()

band1_label = CTkLabel(bands_frame,text="What's the first band's color?",font=("Calibri", 50, "bold"),text_color="#d5f4e6")
band1_buttons = CTkSegmentedButton(bands_frame,values=band_colors[:10],command=band1,width=150,height=90)

band2_label = CTkLabel(bands_frame,text="What's the second band's color?",font=("Calibri", 50, "bold"),text_color="#d5f4e6")
band2_buttons = CTkSegmentedButton(bands_frame,values=band_colors[:10],command=band2,width=150,height=90)

band3_label = CTkLabel(bands_frame,text="What's the third band's color?",font=("Calibri", 50, "bold"),text_color="#d5f4e6")
band3_buttons = CTkSegmentedButton(bands_frame,values=band_colors[:10],command=band3,width=150,height=90)

band4_label = CTkLabel(bands_frame,text="What's the tolerance band's color?",font=("Calibri", 50, "bold"),text_color="#d5f4e6")
band4_buttons = CTkSegmentedButton(bands_frame,values=band_colors[10:],command=band4,width=150,height=90)

root.mainloop()
