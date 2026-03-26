# Setting Up PyCharm for Python Development

PyCharm is a code editor made specifically for Python. It comes in two versions — use the free **Community Edition** for this project. PyCharm is a great choice because it understands Python deeply and handles a lot of setup automatically.

---

## Install PyCharm

1. Go to **https://www.jetbrains.com/pycharm/download/**
2. Scroll down to **PyCharm Community Edition** and click **Download**
3. Run the installer
4. On the installation options screen, check these boxes:
   - **Add "bin" folder to the PATH**
   - **Add "Open Folder as Project"** (lets you right-click a folder and open it in PyCharm)
5. Finish the install and restart your computer if prompted

---

## Open the Project

1. Launch PyCharm
2. On the welcome screen, click **Open**
3. Navigate to your `py-breakout` folder and click **OK**

PyCharm will scan the project and may take a moment to index the files — you'll see a progress bar at the bottom. Wait for it to finish before doing anything else.

---

## Set Up the Virtual Environment

PyCharm can detect and use your existing `.venv` virtual environment, or create one for you.

### If you already created the `.venv` (following the main README)

1. Go to **File → Settings** (or press `Ctrl + Alt + S`)
2. Navigate to **Project: py-breakout → Python Interpreter**
3. Click the **gear icon** (top right of the interpreter box) → **Add Interpreter → Add Local Interpreter**
4. Choose **Existing** on the left
5. Click the `...` button and navigate to `.venv\Scripts\python.exe` inside your project folder
6. Click **OK**

### If you haven't created a virtual environment yet

1. Go to **File → Settings → Project: py-breakout → Python Interpreter**
2. Click the **gear icon → Add Interpreter → Add Local Interpreter**
3. Choose **Virtualenv Environment** on the left, then **New**
4. PyCharm will create a `.venv` inside your project folder automatically
5. Click **OK**, then open the terminal and run:
   ```
   pip install -e .
   ```

Once the interpreter is set, you'll see it listed at the bottom-right of the PyCharm window. It should include `.venv` in the name.

---

## Install Dependencies

If PyCharm notices that `arcade` isn't installed, it may show a banner at the top of `main.py` offering to install missing packages. You can click that, or just run this in the terminal:

```
pip install -e .
```

Open the terminal inside PyCharm with **Alt + F12** (more on the terminal below).

---

## Run the Code

### Option 1 — Right-click

Right-click anywhere inside `breakout/main.py` in the editor and choose **Run 'main'**.

### Option 2 — The Run button

Once you've run it once, a **green play button** appears in the top-right toolbar. Click it any time to run again.

### Option 3 — The terminal

Press **Alt + F12** to open the terminal and type:
```
breakout
```

---

## Understand the PyCharm Layout

```
┌──────────────────────────────────────────────────────┐
│  Menu bar (File, Edit, View, Run...)                 │
├────────┬─────────────────────────────────────────────┤
│        │                                             │
│Project │         Editor (your code)                  │
│  Tree  │                                             │
│        │                                             │
│ (files)├─────────────────────────────────────────────┤
│        │    Run / Terminal / Debug panel              │
└────────┴─────────────────────────────────────────────┘
```

- **Project panel** (left): browse your files and folders
- **Editor** (center): where you write code
- **Run/Terminal panel** (bottom): shows output when you run the program, or a terminal for commands
- **Status bar** (very bottom): shows the current Python interpreter, Git branch, and any warnings

---

## Useful Keyboard Shortcuts

| Shortcut | What it does |
|---|---|
| `Ctrl + S` | Save the current file |
| `Ctrl + Z` | Undo |
| `Ctrl + Shift + Z` | Redo |
| `Ctrl + /` | Comment or uncomment a line |
| `Alt + F12` | Open/close the terminal |
| `Shift + F10` | Run the program |
| `Shift + F9` | Run with debugger |
| `F12` | Go to the definition of a function or variable |
| `Shift + Shift` | Search everywhere (files, actions, settings) |
| `Ctrl + Alt + L` | Auto-format the current file |

> **Tip:** Pressing **Shift** twice (double-shift) opens a search box that can find anything in PyCharm — files, settings, commands. It's the fastest way to find something you can't remember the location of.

---

## Using the Debugger

PyCharm has one of the best debuggers available. It lets you pause your program mid-run and look inside to see exactly what's happening.

**Set a breakpoint:** Click in the grey gutter to the left of any line number. A red circle will appear. When you run with **Shift + F9**, the program will pause there.

While paused, the bottom panel shows:
- **Variables**: every variable in scope and its current value — you can expand lists and objects to inspect them
- **Watches**: variables or expressions you want to track specifically
- **Frames**: the call stack — which functions called which to get here

**Stepping controls** (shown as buttons in the debug panel, or via keyboard):

| Key | What it does |
|---|---|
| `F8` | Step over — run the next line and pause again |
| `F7` | Step into — if the next line calls a function, go inside it |
| `F9` | Resume — continue running until the next breakpoint |

**Evaluate Expression:** While paused, press `Alt + F8` to type any Python expression and see its result instantly — great for testing ideas without editing the code.

---

## Helpful PyCharm Features for Beginners

**Autocomplete:** As you type, PyCharm suggests completions. Press `Tab` or `Enter` to accept one. This saves typing and helps you discover what methods and properties are available.

**Error highlighting:** PyCharm underlines problems as you type — red for errors, yellow for warnings. Hover over the underline to read the explanation.

**Quick fix:** When there's an error, a small red light bulb appears. Click it (or press `Alt + Enter`) to see suggested fixes. PyCharm can often fix common mistakes automatically.

**Rename refactoring:** If you want to rename a variable or function everywhere it's used, right-click the name → **Refactor → Rename** (or press `Shift + F6`). PyCharm updates every reference automatically — much safer than find-and-replace.

**Git integration:** PyCharm has built-in Git support. You can commit, push, and create branches without leaving the editor — go to **Git** in the menu bar. Changed lines are highlighted in the editor gutter in blue, and deleted lines show a small arrow.

---

## Fixing Common Issues

**Red underline under `import arcade`**
PyCharm can't find the arcade library. Check that the correct `.venv` interpreter is selected in **File → Settings → Python Interpreter**. If it's correct, open the terminal and run `pip install -e .`.

**"No Python interpreter configured"**
Go to **File → Settings → Project: py-breakout → Python Interpreter** and add the `.venv` interpreter as described above.

**The terminal doesn't activate the virtual environment automatically**
PyCharm should handle this, but if not, run:
```powershell
.\.venv\Scripts\Activate.ps1
```
or in cmd:
```cmd
.venv\Scripts\activate.bat
```

**PyCharm is slow to start**
This is normal the first time you open a project — PyCharm is indexing all the files so it can provide autocomplete and error checking. It speeds up on subsequent launches.

**Changes don't take effect when I run the program**
Make sure the file is saved (`Ctrl + S`). PyCharm can be configured to save automatically: go to **File → Settings → Appearance & Behavior → System Settings** and check **"Save files automatically if application is idle"**.
