# Emulator Launcher - Features & Development Plan:

## Note: This project is currently under development. For bug reports and suggestions, please provide feedback through the designated reporting system.

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

Emulators allowing cmd game launching:
- Duckstation (https://github.com/stenzek/duckstation/wiki/Command-Line-Arguments)
- PCSX2 (https://pcsx2.net/docs/post/cli/)
- 