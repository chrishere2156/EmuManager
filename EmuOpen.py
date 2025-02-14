import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename
import os

# Gets the current length and width of the window and sets the window to spawn in the middle of the screen
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

# Opens main app window upon launch
def mainScreen():
    selectScreen.title("Emulator Selector") # Sets titlebar name
    selectScreen.geometry("1280x720") # Resolution it displays in

    menubar = tk.Menu(selectScreen) # Add bar at top for menu options

    # Adds the 'Edit' tab
    add = tk.Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Edit', menu = add)
    add.add_command(label ='Add Emulator', command = addEmulator)
    add.add_separator()
    add.add_command(label ='Help', command = help)

    # Adds the 'Options' tab
    opts = tk.Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Options', menu = opts)
    opts.add_command(label ='Settings', command = settings)
    opts.add_command(label ='Exit', command = selectScreen.quit)

    selectScreen.config(menu = menubar) #not sure but without it, it wont work lmao

    # Opens main app window upon launch
    def validate_and_add_entry(EmulatorName, exe_path, game_path, update_link):
        modularEntry(EmulatorName, exe_path, game_path, update_link)

    # Create entries for selected emulators
    for emulator in selected_emulators:
        validate_and_add_entry(
            EmulatorName=emulator['name'],
            exe_path=emulator['exe_path'] if emulator['exe_path'] else None,
            game_path=emulator['game_path'] if emulator['game_path'] else None,
            update_link=emulator['update_link'] if emulator['update_link'] else None
        )

    selectScreen.mainloop() # Nothing above runs until this is reached in code

# This is a modular entry for each emulator. It will be called when a new emulator is added to the list
def modularEntry(EmulatorName, exe_path, game_path, update_link):
    frame = tk.Frame(selectScreen, bd=5, relief="groove", height=50)
    frame.pack_propagate(False)
    frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

    icon = tk.Label(frame, text="Icon", width=10, height=2)
    icon.pack(side=tk.LEFT, padx=5)

    emu_name = tk.Label(frame, text=EmulatorName, width=20, height=2)
    emu_name.pack(side=tk.LEFT, padx=5)

    launch_button = tk.Button(frame, text="Launch Emulator", command=lambda: os.startfile(exe_path), height=2)
    launch_button.pack(side=tk.RIGHT, padx=5)
    
    game_launch_button = tk.Button(frame, text="Launch Game", command=lambda: os.startfile(game_path), height=2)
    game_launch_button.pack(side=tk.RIGHT, padx=5)
    
    update_button = tk.Button(frame, text="Update", command=lambda: os.startfile(update_link), height=2)
    update_button.pack(side=tk.RIGHT, padx=5)

# Screen to explain steps of adding a new emulator to the list
# User picks name
# Where it's stored on computer
# If no icon can be found ask
# Optional box: ask user for download so they can update. Possible to compare versions?
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
    
    # List of emulators
    emulators = [emulator['name'] for emulator in emulator_details]
    emulators.sort()
    
    emulatorListbox = tk.Listbox(presetTab)
    for emulator in emulators:
        emulatorListbox.insert(tk.END, emulator)
    emulatorListbox.pack(pady=10)
    
    # Function to add an emulator based on the selected preset.
    def onSelectPreset(event):
        selectedEmulator = emulatorListbox.get(emulatorListbox.curselection())
        emulator_info = next((emulator for emulator in emulator_details if emulator['name'] == selectedEmulator), None)
        if emulator_info:
            for widget in presetTab.winfo_children():
                widget.destroy()
            tk.Label(presetTab, text=f"Selected Emulator: {selectedEmulator}").pack(pady=10)
            tk.Label(presetTab, text="Emulator EXE Location").pack()
            presetEXE = tk.Entry(presetTab)
            presetEXE.insert(0, emulator_info['exe_path'])
            presetEXE.pack()
            tk.Label(presetTab, text="Game Location").pack()
            presetGameLoc = tk.Entry(presetTab)
            presetGameLoc.insert(0, emulator_info['game_path'])
            presetGameLoc.pack()
            
            # Opens file explorer to select the emulator exe
            def selectExe():
                exe_path = askopenfilename(filetypes=[("Executable files", "*.exe")], parent=presetTab)
                if exe_path:
                    presetEXE.delete(0, tk.END)
                    presetEXE.insert(0, exe_path)
            
            # Opens file explorer to select the game folder
            def selectGameFolder():
                game_path = tk.filedialog.askdirectory(parent=presetTab)
                if game_path:
                    presetGameLoc.delete(0, tk.END)
                    presetGameLoc.insert(0, game_path)
            
            exeButton = tk.Button(presetTab, text="Select EXE", command=selectExe)
            exeButton.pack(pady=5)
            
            gameButton = tk.Button(presetTab, text="Select Game Folder", command=selectGameFolder)
            gameButton.pack(pady=5)

            # Save the preset emulator details to the selectedEmu.txt file
            def savePresetEmulator():
                preset_name = selectedEmulator
                preset_exe_path = presetEXE.get()
                preset_game_path = presetGameLoc.get()
                preset_update_link = emulator_info['update_link']
                
                with open("Emu.txt", 'r') as file:
                    lines = file.readlines()
                
                with open("selectedEmu.txt", 'w') as file:
                    for line in lines:
                        if line.startswith(preset_name + ','):
                            file.write(f"{preset_name},{preset_exe_path},{preset_game_path},{preset_update_link}\n")
                        else:
                            file.write(line)
                
                modularEntry(EmulatorName=preset_name, exe_path=preset_exe_path, game_path=preset_game_path, update_link=preset_update_link)

            tk.Button(presetTab, text="Confirm", command=lambda: savePresetEmulator()).pack(side=tk.RIGHT, padx=5, pady=5)
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
    customExeButton = tk.Button(customTab, text="Select EXE", command=lambda: customExeEntry.insert(0, askopenfilename(filetypes=[("Executable files", "*.exe")], parent=customTab)))
    customExeButton.pack(pady=5)

    tk.Label(customTab, text="Game Location").pack(pady=10)
    customGameEntry = tk.Entry(customTab)
    customGameEntry.pack()
    customGameButton = tk.Button(customTab, text="Select Game Folder", command=lambda: customGameEntry.insert(0, tk.filedialog.askdirectory(parent=customTab)))
    customGameButton.pack(pady=5)

    tk.Label(customTab, text="Update Link (Optional)").pack(pady=10)
    customUpdateEntry = tk.Entry(customTab)
    customUpdateEntry.pack()
    
    # Save the custom emulator details to the selectedEmu.txt file
    def saveCustomEmulator():
        custom_name = customNameEntry.get()
        custom_exe_path = customExeEntry.get()
        custom_game_path = customGameEntry.get()
        custom_update_link = customUpdateEntry.get()
        with open("selectedEmu.txt", 'a') as file:
            file.write(f"{custom_name},{custom_exe_path},{custom_game_path},{custom_update_link}\n")
        modularEntry(EmulatorName=custom_name, exe_path=custom_exe_path, game_path=custom_game_path, update_link=custom_update_link)
    
    tk.Button(customTab, text="Confirm", command=saveCustomEmulator).pack(side=tk.RIGHT, padx=5, pady=5)
    tk.Button(customTab, text="Cancel", command=lambda: None).pack(side=tk.RIGHT, padx=5, pady=5)

# Settings like dark mode, resolution size, font size (maybe), separate tab for emulator list and edit ability.
# It would be wise changing this to have a config file
def settings():
    settingsScreen = tk.Tk()
    settingsScreen.geometry('{}x{}+{}+{}'.format(*windowPos()))
    #emuAdd = askopenfilename()
    #print(emuAdd)
    settingsScreen.mainloop()

# For the 'Help' option. Only a placeholder at the moment so I can test functions easily
def help():
    print(windowPos())

# Function to read emulator details from a text file
def read_emulators(file_path):
    emulators = []
    with open(file_path, 'r') as file:
        for line in file:
            details = line.strip().split(',')
            if len(details) == 4:
                emulators.append({
                    'name': details[0],
                    'exe_path': details[1],
                    'game_path': details[2],
                    'update_link': details[3]
                })
    return emulators

# SETUP PART
# Load emulator details from the text file
emulator_details = read_emulators('EMU.txt')
# Load selected emulator details from the text file
selected_emulators = read_emulators('selectedEmu.txt')
# This is needed to define the main window. Better to be outside of mainScreen function to be accessed by other functions
selectScreen = tk.Tk() 

#Program starts here. This is the first function that runs
mainScreen()