import tkinter as tk
from tkinter import StringVar, font as tkFont
from tkinter.constants import FALSE, TRUE
import serial as ser

xBee = ser.Serial('COM5', 57600)

def pourWG():
    global sizeVar, statString
    pour = sizeVar.get()
    print("pouring whisky ginger, " + pour)
    statString.set("pouring whisky ginger, " + pour)
    xBee.write(b'J')
    pourD = True
    while pourD:
        if xBee.in_waiting:
            cmd = xBee.readline()
            string = cmd.decode("ascii")
            string = string.rstrip("\n")
            statString.set("Done pouring")
            pourD = False

def pourMarg():
    global sizeVar, statString
    pour = sizeVar.get()
    print("pouring margarita, " + pour)
    statString.set("pouring margarita, " + pour)

def pourHigh():
    global sizeVar, statString
    pour = sizeVar.get()
    print("pouring highball, " + pour)
    statString.set("pouring highball, " + pour)

def pourTeq():
    global sizeVar, statString
    pour = sizeVar.get()
    print("pouring tequila highball, " + pour)
    statString.set("pouring tequila highball, " + pour)

root = tk.Tk()
root.title("Inebriator 3000")
root.geometry('1920x1280')
#root.attributes('-zoomed', True)
root.config(bg='#003049')
root.grid_rowconfigure(0, weight=1) # For row 0
root.grid_rowconfigure(1, weight=1) # For row 1
root.grid_rowconfigure(2, weight=1) # For row 2
root.grid_columnconfigure(0, weight=1) # For column 0
root.grid_columnconfigure(1, weight=1) # For column 1

header = tk.Label(root, text='Select Size and Drink:', bg='red', fg='#EAE2B7', font=("Arial", 40))
header.grid(row=0,column=0)

sizeVar = tk.StringVar(root)
sizeVar.set("Single")
size = tk.OptionMenu(root, sizeVar, "Single", "Double")
size.grid(row=0,column=1)
size.config(bg='red', fg='#EAE2B7', font=("Arial", 40))
style = tkFont.Font(family='Arial', size=35)
menu = root.nametowidget(size.menuname)
menu.config(font=style)

whiskyGinger = tk.Button(root, text="Whisky Ginger", command=pourWG, bg='red', fg='#EAE2B7', font=("Arial", 28), height=5, width=21)
whiskyGinger.grid(row=1, column=0)

margarita = tk.Button(root, text="Margarita", command=pourMarg, bg='red', fg='#EAE2B7', font=("Arial", 28), height=5, width=21)
margarita.grid(row=1, column=1)

highball = tk.Button(root, text="highball", command=pourHigh, bg='red', fg='#EAE2B7', font=("Arial", 28), height=5, width=21)
highball.grid(row=2, column=0)

teqHigh = tk.Button(root, text="tequila highball", command=pourTeq, bg='red', fg='#EAE2B7', font=("Arial", 28), height=5, width=21)
teqHigh.grid(row=2, column=1)

status = tk.Label(root, text="Inebriator 3000 Status:", bg='red', fg='#EAE2B7', font=("Arial", 20))
status.grid(row=3, column=0)

statString = StringVar()
statString.set("waiting for order")
statDisplay = tk.Label(root, bg='red', fg='#EAE2B7', font=('Arial', 20), textvariable=statString)
statDisplay.grid(row=3, column=1)


root.mainloop()
