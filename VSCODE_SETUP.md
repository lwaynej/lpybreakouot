# Setting Up VS Code for Python Development

Visual Studio Code (VS Code) is a free code editor made by Microsoft. It's one of the most popular tools for writing Python and works great on Windows. This guide walks you through getting it set up for this project.

---

## Install VS Code

1. Go to **https://code.visualstudio.com/**
2. Click **"Download for Windows"**
3. Run the installer — leave all options at their defaults, but it's worth checking **"Add to PATH"** if that option appears

When it's done, open VS Code from the Start menu.

---

## Open the Project

1. In VS Code, go to **File → Open Folder**
2. Navigate to your `py-breakout` folder and click **"Select Folder"**

You'll see the project files listed in the **Explorer panel** on the left side.

---

## Install the Python Extension

VS Code doesn't know about Python by default — you need to add the official extension.

1. Click the **Extensions icon** on the left sidebar (it looks like four squares)
2. In the search box, type `Python`
3. Find the one published by **Microsoft** (it will be the top result)
4. Click **Install**

This extension gives you syntax highlighting, error detection, autocomplete, and the ability to run Python files directly inside VS Code.

While you're here, also install these two extensions — they're very helpful:

| Extension | Publisher | What it does |
|---|---|---|
| **Pylance** | Microsoft | Smarter autocomplete and error checking |
| **Ruff** | Astral Software | Automatically highlights code style issues |

---

## Select the Python Interpreter

VS Code needs to know which Python to use — specifically the one inside your virtual environment.

1. Open the **Command Palette** with `Ctrl + Shift + P`
2. Type `Python: Select Interpreter` and press Enter
3. You should see a list of Python versions. Look for one that includes `.venv` in the path, something like:
   ```
   Python 3.x.x ('.venv': venv)
   ```
4. Select that one

> **Why this matters:** If you pick the wrong interpreter, VS Code won't find the `arcade` library and will show red error lines even though nothing is actually wrong with your code.

Once selected, you'll see the Python version shown in the **bottom-right corner** of VS Code. It should show `.venv`.

---

## The Integrated Terminal

VS Code has a built-in terminal so you don't need to switch to a separate PowerShell or cmd window.

Open it with **Ctrl + `** (the backtick key, top-left of the keyboard under Escape).

When VS Code knows about your virtual environment, it will **activate it automatically** when you open the terminal. You'll see `(.venv)` at the prompt without having to type the activate command yourself.

From the terminal you can run:
```
breakout
```

---

## Run the Code Directly from VS Code

With the Python extension installed, you can run your code without using the terminal at all:

1. Open `breakout/main.py` by clicking it in the Explorer panel
2. Press **F5** — this starts the program in debug mode (more on that below)

Or, for a simpler run with no debug tools attached, press **Ctrl + F5**.

---

## Understand the VS Code Layout

```
┌──────────────────────────────────────────────────────┐
│  Menu bar (File, Edit, View...)                      │
├────────┬─────────────────────────────────────────────┤
│        │                                             │
│Explorer│         Editor (your code)                  │
│        │                                             │
│ (files)│                                             │
│        ├─────────────────────────────────────────────┤
│        │         Terminal                            │
└────────┴─────────────────────────────────────────────┘
```

- **Explorer** (left): browse and open files
- **Editor** (center): where you write code
- **Terminal** (bottom): where you run commands
- **Status bar** (very bottom): shows your Python interpreter, Git branch, and errors

---

## Useful Keyboard Shortcuts

| Shortcut | What it does |
|---|---|
| `Ctrl + S` | Save the current file |
| `Ctrl + Z` | Undo |
| `Ctrl + Shift + Z` | Redo |
| `Ctrl + /` | Comment or uncomment a line |
| `Ctrl + \`` | Open/close the terminal |
| `Ctrl + Shift + P` | Open the Command Palette (search for any VS Code action) |
| `F5` | Run with debugger |
| `Ctrl + F5` | Run without debugger |
| `F12` | Go to the definition of a function or variable |
| `Ctrl + P` | Quickly open any file by name |

---

## Using the Debugger

The debugger lets you pause your program at any line and inspect what's happening inside — very useful when something isn't working as expected.

**Set a breakpoint:** Click in the grey area to the left of a line number. A red dot will appear. When you run with **F5**, the program will pause at that line.

While paused, you can:
- Hover over a variable to see its current value
- Use the **Variables panel** (left side) to see all values at once
- Press **F10** to step forward one line at a time
- Press **F5** again to continue running until the next breakpoint

---

## Fixing Common Issues

**Red squiggly lines under `import arcade`**
VS Code can't find the arcade library. Make sure you've selected the `.venv` interpreter (see "Select the Python Interpreter" above).

**The terminal doesn't show `(.venv)`**
Open a new terminal with **Ctrl + `**. If it still doesn't activate, manually run:
```powershell
.\.venv\Scripts\Activate.ps1
```
or in cmd:
```cmd
.venv\Scripts\activate.bat
```

**Changes to the code don't seem to do anything**
Make sure you saved the file with `Ctrl + S` before running.

**VS Code is asking which interpreter to use every time**
This usually means the `.venv` folder isn't in the project folder. Check that you created the virtual environment while inside the `py-breakout` folder.
