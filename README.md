# Emulator Launcher - Features & Development Plan:

## Note: This project is currently under development. For bug reports and suggestions, please provide feedback through the designated reporting system.

## Installation:


## How To Use:
#### After downloading the program to your computer these are the steps to add your first emulator.
### Step 1:
Below is what the program will look like from first launch.

![Screenshot 2025-02-14 225728](https://github.com/user-attachments/assets/6e7a5483-3f4c-46a0-82e9-963852bebf10)

### Step 2:
On the top left a click the **"edit"** menu option and click **"add emulator"**.

![Screenshot 2025-02-14 225742](https://github.com/user-attachments/assets/5c2a7c63-bba6-4224-b218-30fc68599d81)

### Step 3 A1:
A new window new will open revealing preset and custom choices. i will cover preset first. <br/>
You will see preset options (currently only xenia avalible) click the one you want to add.

![Screenshot 2025-02-14 225748](https://github.com/user-attachments/assets/71bfc056-bc2a-46cf-8b5d-9b8b2ca214f1)

### Step 3 A2:
1. Now you will need to add the location of your existing emulator path. you can click the **"select exe"** for easier finding.
2. You can also add your games to this program by selecting the folder containing all the games for that one emulator.
3. Click confirm when finshed and go to Step 4.

![Screenshot 2025-02-14 225811](https://github.com/user-attachments/assets/c5e97481-f9b4-4351-a9d0-3a4edd1a76ae)

### Step 3 B1:
1. For a custom or not yet added emulator select the custom tab at the top.
2. Put the name of the emulator in the first box.
3. Then select the location of your existing emulator path. you can click the **"select exe"** for easier finding.
4. If you need you can also add your games to this program by selecting the folder containing all the games for that one emulator.
5. Finally optionally you can add the web page link to update your emulator so you can one click update inside the program.
6. Press Confirm, you always can change these setting later if you make a mistake.

![Screenshot 2025-02-14 225756](https://github.com/user-attachments/assets/6401cb56-05e6-4d39-a0a8-509f5e116ff3)

### Step 4:
Congrats you have added an emulator to the program. after confirm is pressed a new entry is spawned in the main window. <br/>
- Now you can launch it by pressing launch button,
- update the program with one click (if setup),
- use the game selector to play your games without opening the actual emulator GUI first.

![Screenshot 2025-02-14 225824](https://github.com/user-attachments/assets/a365658b-a4fb-4c25-b162-5ba909e0df27)

### Purpose of the Interface:
#### This launcher is designed to manage multiple emulators, allowing users to:
- Easily add, update, and launch emulators.
- Support multiple configuration instances (for emulators like Xenia).
- Provide a clean, user-friendly UI with customization options.

### Main Features & Enhancements
#### Emulator List (Main Page)
Pinned Emulators (Users can pin frequently used ones to the top)

Search & Filter (Quickly find an emulator)

Each emulator entry includes:
- Icon & Name
- Update Button (Checks for and installs updates)
- Launch Button (Starts the emulator)
- in later updates a drop down arrow to select like custom instance like with xenia configs

#### "Add Emulator" System
If no emulators are added, the main page shows a message guiding users to the Add option.

From this menu option Users can either:
- Select from predefined emulators (Auto-fills settings).
- Manually add a custom emulator (Custom name, update method, etc.).
- Drag & Drop Support (Maybe – only if it’s not too complex)

#### Portable
The program will run in one place so you can easily move its location with no affect.


## EXTRA DEV Notes:

### Menu Options
#### Edit Menu:
Add Emulator (Opens the emulator setup window).

Help (Optional – might not be needed).

#### Options Menu:
Settings (Editable via UI & External Config File)
General: Dark mode, font size, resolution

Emulators: List of added emulators, Edit file location, change icon, rename emulator, Direct link to the emulator’s website, Search & Filter for added emulators

Appearance: UI Themes (Light, Dark, and potentially more).

Exit: Closes the program.



## Future Expansion Ideas (Optional but Interesting)

These are ideas that might be worth considering later:

Custom UI Themes (Beyond Light/Dark mode).

Recent Games List (If launching games ever becomes possible).

Cloud Sync for Settings (Useful for multiple PCs, but complex).

Plugin System (For user scripts and automation features).

Launch game from the UI (i have a feeling only some emulator allow it)

Emulators researched:
- Duckstation (https://github.com/stenzek/duckstation/wiki/Command-Line-Arguments)
- PCSX2 (https://pcsx2.net/docs/post/cli/)
- RPCS3 I cant find a link but people have mentioned and it seem possible
- ShadPS4 (no wiki, but i tested it and it works)
- xemu (https://xemu.app/docs/cli/)
- xenia (select exe and then path to game. works with shortcut)
