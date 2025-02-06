import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename

selectScreen = tk.Tk() # this tells the program to create a window

#this is a modular entry for each emulator. it will be called when a new emulator is added to the list
def modularEntry(EmulatorName):
    frame = tk.Frame(selectScreen, bd=5, relief="groove")
    frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

    icon = tk.Label(frame, text="Icon", width=10)
    icon.pack(side=tk.LEFT, padx=5)

    emu_name = tk.Label(frame, text=EmulatorName, width=20)
    emu_name.pack(side=tk.LEFT, padx=5)

    launch_button = tk.Button(frame, text="Launch Emulator", command=lambda: None)
    launch_button.pack(side=tk.RIGHT, padx=5)
    
    game_launch_button = tk.Button(frame, text="Launch Game", command=lambda: None)
    game_launch_button.pack(side=tk.RIGHT, padx=5)
    
    update_button = tk.Button(frame, text="Update", command=lambda: None)
    update_button.pack(side=tk.RIGHT, padx=5)

# Opens main app window apon launch
def mainScreen():
    selectScreen.title("Emulator Selector") #sets titlebar name
    selectScreen.geometry("1280x720") #resoultion it displays in (change this later to open to a settings dependent size that user can pick)

    menubar = tk.Menu(selectScreen) #add bar at top for menu options

    #adds the 'Edit' tab
    add = tk.Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Edit', menu = add)
    add.add_command(label ='Add Emulator', command = addEmulator)
    add.add_separator()
    add.add_command(label ='Help', command = help)

    #adds the 'Options' tab
    opts = tk.Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Options', menu = opts)
    opts.add_command(label ='Settings', command = settings)
    opts.add_command(label ='Exit', command = selectScreen.quit)

    selectScreen.config(menu = menubar) #not sure but without it, it wont work lmao
    selectScreen.mainloop() #nothing above runs untill this is reached in code

#screen to explain steps of adding a new emulator to the list
#user picks name
#where its stored on computer
#if no icon can be found ask
#optional box: ask user for download so they can update. possible to compare versions?
def addEmulator():
    global addScreen
    if 'addScreen' in globals() and addScreen.winfo_exists():
        addScreen.destroy()
    addScreen = tk.Toplevel(selectScreen)
    addScreen.title("Add Emulator")
    #addScreen.geometry("500x500")
    addScreen.geometry('{}x{}+{}+{}'.format(*windowPos()))

    # Tabs for preset and custom emulators
    tabControl = tk.ttk.Notebook(addScreen)
    
    # Preset Emulator Tab
    presetTab = tk.Frame(tabControl, relief="groove", bd=5)
    tabControl.add(presetTab, text='Preset Emulator')
    
    # Custom Emulator Tab
    customTab = tk.Frame(tabControl, relief="groove", bd=5)
    tabControl.add(customTab, text='Custom Emulator')
    
    tabControl.pack(expand=1, fill="both")
    
    # Preset Emulator Tab Content
    presetLabel = tk.Label(presetTab, text="Select an Emulator from the list")
    presetLabel.pack(pady=10)
    
    # List of emulators (example list, replace with actual file reading)
    emulators = ["Emulator1", "Emulator2", "Emulator3"]
    emulators.sort()
    
    emulatorListbox = tk.Listbox(presetTab)
    for emulator in emulators:
        emulatorListbox.insert(tk.END, emulator)
    emulatorListbox.pack(pady=10)
    
    def onSelectPreset(event):
        selectedEmulator = emulatorListbox.get(emulatorListbox.curselection())
        for widget in presetTab.winfo_children():
            widget.destroy()
        tk.Label(presetTab, text=f"Selected Emulator: {selectedEmulator}").pack(pady=10)
        tk.Label(presetTab, text="Emulator EXE Location").pack()
        exeEntry = tk.Entry(presetTab)
        exeEntry.pack()
        tk.Label(presetTab, text="Game Location").pack()
        gameEntry = tk.Entry(presetTab)
        gameEntry.pack()
        
        def selectExe():
            exe_path = askopenfilename(filetypes=[("Executable files", "*.exe")], parent=presetTab)
            if exe_path:
                exeEntry.delete(0, tk.END)
                exeEntry.insert(0, exe_path)
        
        def selectGameFolder():
            game_path = tk.filedialog.askdirectory(parent=presetTab)
            if game_path:
                gameEntry.delete(0, tk.END)
                gameEntry.insert(0, game_path)
        
        exeButton = tk.Button(presetTab, text="Select EXE", command=selectExe)
        exeButton.pack(pady=5)
        
        gameButton = tk.Button(presetTab, text="Select Game Folder", command=selectGameFolder)
        gameButton.pack(pady=5)

        tk.Button(presetTab, text="Confirm", command=lambda: None).pack(side=tk.RIGHT, padx=5, pady=5)
        tk.Button(presetTab, text="Cancel", command=lambda: None).pack(side=tk.RIGHT, padx=5, pady=5)
        tk.Button(presetTab, text="Back", command=lambda: addEmulator()).pack(side=tk.RIGHT, padx=5, pady=5)
    
    emulatorListbox.bind('<<ListboxSelect>>', onSelectPreset)
    
    # Custom Emulator Tab Content
    tk.Label(customTab, text="Name of Emulator").pack(pady=10)
    customNameEntry = tk.Entry(customTab)
    customNameEntry.pack()
    
    tk.Label(customTab, text="Emulator EXE Location").pack(pady=10)
    customExeEntry = tk.Entry(customTab)
    customExeEntry.pack()
    
    tk.Label(customTab, text="Game Location").pack(pady=10)
    customGameEntry = tk.Entry(customTab)
    customGameEntry.pack()
    
    tk.Label(customTab, text="Update Link (Optional)").pack(pady=10)
    customUpdateEntry = tk.Entry(customTab)
    customUpdateEntry.pack()
    
    tk.Button(customTab, text="Confirm", command=lambda: None).pack(side=tk.RIGHT, padx=5, pady=5)
    tk.Button(customTab, text="Cancel", command=lambda: None).pack(side=tk.RIGHT, padx=5, pady=5)

#settings like dark mode, resolution size, font size(maybe), seperate tab for emulator list and edit ability.
#it would be wise changing this to have a config file
def settings():
    settingsScreen = tk.Tk()
    settingsScreen.geometry('{}x{}+{}+{}'.format(*windowPos()))
    #emuAdd = askopenfilename()
    #print(emuAdd)
    settingsScreen.mainloop()

#for the 'Help' option. only a placeholder at the moment so i can test functions easily
def help():
    print(windowPos())

#gets the current length and width of the window and sets the window to spawn in the middle of the screen
def windowPos():
    selectScreen.update_idletasks()
    x = selectScreen.winfo_x()
    y = selectScreen.winfo_y()
    width = selectScreen.winfo_width()
    height = selectScreen.winfo_height()
    new_width = 500
    new_height = 500
    new_x = x + (width // 2) - (new_width // 2)
    new_y = y + (height // 2) - (new_height // 2)
    return new_width, new_height, new_x, new_y

mainScreen() #runs whole program
