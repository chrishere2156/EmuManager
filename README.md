Emulator Launcher - Features & Development Plan

Note: This project is currently under development.

1. Purpose of the Interface
This launcher is designed to manage multiple emulators, allowing users to:
Easily add, update, and launch emulators.
Support multiple configuration instances (for emulators like Xenia).
Provide a clean, user-friendly UI with customization options.

2. Main Features & Enhancements
A) Emulator List (Main Page)
Each emulator entry includes:
Icon & Name
Update Button (Checks for and installs updates)
Launch Button (Starts the emulator)
Pinned Emulators (Users can pin frequently used ones to the top)
Search & Filter (Quickly find an emulator)
Sorting Options (Default: A-Z, Optional: Last Used)

B) "Add Emulator" System
If no emulators are added, the main page shows a message guiding users to the Add option.
Users can either:
Select from predefined emulators (Auto-fills settings).
Manually add a custom emulator (Custom name, update method, etc.).
Drag & Drop Support (Maybe – only if it’s not too complex)

C) Emulator Detection
When adding emulators, users can scan a specified folder for existing emulators.

D) Portable Mode
All settings & emulators should be able to run from a single folder (great for USB drives or multiple PCs).

3. Menu Options

Edit Menu:
Add Emulator (Opens the emulator setup window).
Help (Optional – might not be needed).

Options Menu:
1. Settings (Editable via UI & External Config File)
General:
Dark mode,
font size,
resolution

Emulators:
List of added emulators
Edit file location, change icon, rename emulator
Direct link to the emulator’s website
Search & Filter for added emulators

Appearance:
UI Themes (Light, Dark, and potentially more).

3. Exit
Closes the program.

4. Future Expansion Ideas (Optional but Interesting)

These are ideas that might be worth considering later:

Custom UI Themes (Beyond Light/Dark mode).
Recent Games List (If launching games ever becomes possible).
Cloud Sync for Settings (Useful for multiple PCs, but complex).
Plugin System (For user scripts and automation features).
