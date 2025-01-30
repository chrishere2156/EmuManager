import tkinter as tk
from tkinter.filedialog import askopenfilename

# Create a new window
def mainScreen():
    selectScreen = tk.Tk()

    selectScreen.title("Emulator Selector")
    selectScreen.geometry("1280x720")

    menubar = tk.Menu(selectScreen)

    add = tk.Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Edit', menu = add)
    add.add_command(label ='Add Emulator', command = addEmulator)
    add.add_separator()
    add.add_command(label ='Help', command = None)

    opts = tk.Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Options', menu = opts)
    opts.add_command(label ='Settings', command = None)
    opts.add_command(label ='Exit', command = selectScreen.quit)

    selectScreen.config(menu = menubar)
    selectScreen.mainloop()

def addEmulator():
    emuAdd = askopenfilename()
    print(emuAdd)

def settings():
    pass

def openWindow():
    newWindow = 

def help():
    pass

mainScreen()
