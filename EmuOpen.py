import tkinter as tk
from tkinter.filedialog import askopenfilename

# Opens main app window apon launch
def mainScreen():
    selectScreen = tk.Tk() # this tells the program to create a window

    selectScreen.title("Emulator Selector") #sets titlebar name
    selectScreen.geometry("1280x720") #resoultion it displays in (change this later to open to a settings dependent size that user can pick)

    menubar = tk.Menu(selectScreen) #add bar at top for menu options

    #adds the 'Edit' tab
    add = tk.Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Edit', menu = add)
    add.add_command(label ='Add Emulator', command = addEmulator)
    add.add_separator()
    add.add_command(label ='Help', command = None)

    #adds the 'Options' tab
    opts = tk.Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Options', menu = opts)
    opts.add_command(label ='Settings', command = None)
    opts.add_command(label ='Exit', command = selectScreen.quit)

    selectScreen.config(menu = menubar) #not sure but without it, it wont work lmao
    selectScreen.mainloop() #nothing above runs untill this is reached in code

#screen to explain steps of adding a new emulator to the list
#user picks name
#where its stored on computer
#if no icon can be found ask
#optional box: ask user for download so they can update. possible to compare versions?
def addEmulator():
    addEmu = tk.Tk()
    #emuAdd = askopenfilename()
    #print(emuAdd)
    addEmu.mainloop()

#settings like dark mode, resolution size, font size(maybe), seperate tab for emulator list and edit ability.
#it would be wise changing this to have a config file
def settings():
    settingsScreen = tk.Tk()
    #emuAdd = askopenfilename()
    #print(emuAdd)
    settingsScreen.mainloop()

#this is only here for test. i think ill need seperate openwindow for each task
#def openWindow():
    #newWindow = 
    #pass

#for the 'Help' option. only a placeholder as i hope i dont need to explain
def help():
    pass

mainScreen() #runs whole program
