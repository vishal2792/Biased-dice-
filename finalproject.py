import tkinter
import random
window = tkinter.Tk()
window.geometry("800x800")
window.title('Biased Dice')
icon1 = tkinter.PhotoImage(file="C:/Users/vishal/OneDrive/Pictures/Screenshots/dice 1.png")
icon2 = tkinter.PhotoImage(file="C:/Users/vishal/OneDrive/Pictures/Screenshots/dice 2.png")
icon3 = tkinter.PhotoImage(file="C:/Users/vishal/OneDrive/Pictures/Screenshots/dice 3.png")
icon4 = tkinter.PhotoImage(file="C:/Users/vishal/OneDrive/Pictures/Screenshots/dice 4.png")
icon5 = tkinter.PhotoImage(file="C:/Users/vishal/OneDrive/Pictures/Screenshots/dice 5.png")
icon6 = tkinter.PhotoImage(file="C:/Users/vishal/OneDrive/Pictures/Screenshots/dice 6n.png")


def roll_dice1():
    n = random.randint(1, 6)
    if n == 1:
        label = tkinter.Label(window, image=icon1)
        label.pack()
    elif n == 2:
        label = tkinter.Label(window, image=icon2)
        label.pack()
    elif n == 3:
        label = tkinter.Label(window, image=icon3)
        label.pack()
    elif n == 4:
        label = tkinter.Label(window, image=icon4)
        label.pack()
    elif n == 5:
        label = tkinter.Label(window, image=icon5)
        label.pack()
    elif n == 6:
        label = tkinter.Label(window, image=icon6)
        label.pack()


button = tkinter.Button(window, text='roll regular dice ', foreground='black', command=roll_dice1)
button.pack()


def roll_dice2():
    x = random.randint(1, 100)
    if x <= 50:
        n = 1
    else:
        n = random.randint(2, 6)
    if n == 1:
        label = tkinter.Label(window, image=icon1)
        label.pack()
    elif n == 2:
        label = tkinter.Label(window, image=icon2)
        label.pack()
    elif n == 3:
        label = tkinter.Label(window, image=icon3)
        label.pack()
    elif n == 4:
        label = tkinter.Label(window, image=icon4)
        label.pack()
    elif n == 5:
        label = tkinter.Label(window, image=icon5)
        label.pack()
    elif n == 6:
        label = tkinter.Label(window, image=icon6)
        label.pack()


button = tkinter.Button(window, text='dice with 0.5 probability of 1', foreground='black', command=roll_dice2)
button.pack()


def roll_dice3():
    x = random.randint(1, 100)
    if x <= 50:
        n = 6
    else:
        n = random.randint(1, 5)
    if n == 1:
        label = tkinter.Label(window, image=icon1)
        label.pack()
    elif n == 2:
        label = tkinter.Label(window, image=icon2)
        label.pack()
    elif n == 3:
        label = tkinter.Label(window, image=icon3)
        label.pack()
    elif n == 4:
        label = tkinter.Label(window, image=icon4)
        label.pack()
    elif n == 5:
        label = tkinter.Label(window, image=icon5)
        label.pack()
    elif n == 6:
        label = tkinter.Label(window, image=icon6)
        label.pack()


button = tkinter.Button(window, text='dice with 0.5 probability of 6', foreground='black', command=roll_dice3)
button.pack()
window.mainloop()