# Breakout Game

Welcome! This project is a first step toward building a classic Breakout game in Python. Right now it opens a graphics window and displays "Hello World" — a tradition in programming that means you've got everything working and you're ready to build something.

## Additional Guides

| Guide                               | Description                                          |
|-------------------------------------|------------------------------------------------------|
| [VS Code Setup](VSCODE_SETUP.md)    | Setting up Visual Studio Code for Python development |
| [PyCharm Setup](PYCHARM_SETUP.md)   | Setting up PyCharm for Python development            |
| [Markdown Guide](MARKDOWN_GUIDE.md) | How to format `.md` files like this one              |

---

## Step 1 — Install Python

Python is the programming language this project uses. If you don't have it yet:

1. Go to **https://www.python.org/downloads/**
2. Click the big yellow **"Download Python"** button
3. Run the installer
4. **Important:** On the first screen of the installer, check the box that says **"Add Python to PATH"** before clicking Install

To check that it worked, open **PowerShell** (press `Win + S`, type `powershell`, press Enter) and type:

```powershell
py --version
```

You should see something like `Python 3.13.1`. If you do, you're good to go.

---

## Step 2 — Download this Project

If you received this as a zip file, unzip it somewhere easy to find, like your Desktop or Documents folder.

Then open PowerShell and navigate to the project folder. For example, if you put it on your Desktop:

```powershell
cd "$env:USERPROFILE\Desktop\py-breakout"
```

> **Tip:** You can type `cd ` and then drag the folder into the PowerShell window — it will fill in the path for you.

---

## Step 3 — Create a Virtual Environment

A **virtual environment** is a private, isolated copy of Python just for this project. This means any libraries you install here won't interfere with other Python projects, and vice versa. It's a good habit to always use one.

Create it by running:

```powershell
py -m venv .venv
```

This creates a hidden folder called `.venv` inside your project. You only need to do this once.

---

## Step 4 — Activate the Virtual Environment

Every time you open a new PowerShell window to work on this project, you need to **activate** the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

When it's active, you'll see `(.venv)` at the beginning of your prompt, like this:

```
(.venv) PS C:\Users\YourName\Desktop\py-breakout>
```

That's how you know it's working.

> **Troubleshooting:** If PowerShell says "running scripts is disabled", run this command first:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```
> Then try activating again.

---

## Step 5 — Install the Project

Now install the project and its dependencies (the extra libraries it needs) with one command:

```powershell
pip install -e .
```

This reads `pyproject.toml` to find out what the project needs and installs everything automatically. The `-e` means "editable" — any changes you make to the code take effect immediately without reinstalling.

The main library this installs is **Arcade**, which handles the graphics window, drawing, and eventually game logic like movement and collisions.

---

## Step 6 — Run It

```powershell
breakout
```

A window should appear with a black background and "Hello World" written in white text in the center. Close it with the X button when you're done.

---

## What the Code Does

Open `breakout/main.py` and you'll see this:

```python
import arcade
```
This loads the Arcade library so we can use its tools for drawing and creating windows.

```python
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Breakout"
```
These are **constants** — values that stay the same throughout the program. The window will be 640 pixels wide and 480 pixels tall.

```python
class BreakoutGame(arcade.Window):
```
This creates a **class** — a blueprint for our game. It inherits from `arcade.Window`, which means it gets all the built-in window behavior for free, and we just add our own customizations on top.

```python
def __init__(self):
    super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.BLACK)
```
`__init__` runs automatically when the game starts. It sets up the window size and makes the background black.

```python
def on_draw(self):
    self.clear()
    arcade.draw_text("Hello World", ...)
```
`on_draw` is called by Arcade every frame to draw the screen. First it clears the screen, then draws "Hello World" centered in the window.

```python
def main():
    BreakoutGame()
    arcade.run()
```
`main()` creates the game and hands control to Arcade, which runs the game loop — a continuous cycle of drawing and checking for events (like key presses) that keeps the window alive.

---

## Project Structure

```
py-breakout/
├── breakout/
│   ├── __init__.py   # marks this folder as a Python package
│   └── main.py       # all the game code lives here for now
├── pyproject.toml    # project settings and list of dependencies
├── .gitignore        # tells Git which files to leave out
└── README.md         # this file
```

## The .gitignore File

Not everything in your project folder should be uploaded to GitHub. The `.gitignore` file tells Git which files and folders to ignore — they stay on your machine but are never committed or pushed.

For this project, `.gitignore` excludes:

- **`.venv/`** — your virtual environment. This folder can be hundreds of megabytes and is easily recreated with `pip install -e .`, so there's no reason to upload it. Everyone who clones the project creates their own.
- **`__pycache__/` and `*.pyc`** — files Python generates automatically when it runs your code. They're not source code and change constantly, so they'd create noisy, meaningless commits.
- **`*.egg-info/`, `dist/`, `build/`** — folders created when packaging the project. Generated automatically, not hand-written.
- **`.vscode/` and `.idea/`** — editor settings folders for VS Code and PyCharm. These contain personal preferences that vary between developers and shouldn't be forced on collaborators.
- **`Thumbs.db`, `desktop.ini`** — hidden files Windows creates automatically in folders. They have nothing to do with your code.
- **`.DS_Store`** — a hidden file macOS creates in every folder. Included here since the project has collaborators on Mac.

A good rule of thumb: if a file is **generated automatically** or contains **personal settings**, it probably belongs in `.gitignore`.

---

## Using Command Prompt (cmd) Instead of PowerShell

If you prefer the classic Command Prompt over PowerShell, everything works the same except for a couple of differences.

Open Command Prompt by pressing `Win + S`, typing `cmd`, and pressing Enter.

**Navigate to the project folder:**
```cmd
cd %USERPROFILE%\Desktop\py-breakout
```

**Create the virtual environment** (same as PowerShell):
```cmd
py -m venv .venv
```

**Activate the virtual environment** — this is the main difference from PowerShell:
```cmd
.venv\Scripts\activate.bat
```

You'll see `(.venv)` appear at the start of your prompt, just like in PowerShell. From here, all other commands (`pip install -e .`, `breakout`, etc.) are identical.

> **Note:** The PowerShell execution policy issue does not apply to cmd. If PowerShell gave you trouble, cmd is a simple alternative.

---

## Every Time You Come Back

Each new session, just remember:

1. Open PowerShell or Command Prompt and navigate to the project folder
2. Activate the virtual environment:
   - PowerShell: `.\.venv\Scripts\Activate.ps1`
   - Command Prompt: `.venv\Scripts\activate.bat`
3. Run the game: `breakout`

You only need to run `pip install -e .` once (or again if the dependencies change).

---

## Working with Git and GitHub

Git is a tool that tracks changes to your code over time. GitHub is a website where you can store your code online and collaborate with others. Together they let you save your work, experiment safely, and contribute to other people's projects.

### Install Git

If you don't have Git, download it from **https://git-scm.com/downloads** and run the installer. You can leave all the options at their defaults.

Check that it worked:
```cmd
git --version
```

### Fork the Project on GitHub

A **fork** is your own personal copy of someone else's project on GitHub. You can make changes to your fork freely without affecting the original. When you're happy with your changes, you can send them back as a **pull request**.

1. Go to the project page on GitHub
2. Click the **Fork** button in the top-right corner
3. GitHub will create a copy of the project under your own account

Now clone your fork to your computer (replace `your-username` with your GitHub username):

```cmd
git clone https://github.com/your-username/py-breakout.git
cd py-breakout
```

This downloads the project to your machine and puts you inside the folder.

### Understand the Basic Workflow

Every time you want to make a change, follow this pattern:

```
create a branch → make your changes → commit → push → open a pull request
```

Never make changes directly on the `main` branch. Always create a new branch first — this keeps your work organized and makes it easy for others to review.

### Create a Branch

A **branch** is like a separate workspace where you can make changes without touching the main code. Give it a short descriptive name:

```cmd
git checkout -b add-paddle
```

This creates a new branch called `add-paddle` and switches to it. You can name it anything that describes what you're working on.

To see which branch you're currently on:

```cmd
git branch
```

The branch with a `*` next to it is the active one.

### Make Your Changes

Edit the code in `breakout/main.py` (or any other file). When you're ready, check what you've changed:

```cmd
git status
```

This shows which files have been modified. To see the actual line-by-line changes:

```cmd
git diff
```

### Commit Your Changes

A **commit** is a snapshot of your work saved to the history. First, tell Git which files to include:

```cmd
git add breakout/main.py
```

To include all changed files at once:

```cmd
git add .
```

Then save the snapshot with a short message describing what you did:

```cmd
git commit -m "Add paddle to the bottom of the screen"
```

Write your commit messages like a sentence finishing "This commit will..." — keep them short and specific.

### Push to GitHub

Sending your commits up to GitHub is called **pushing**:

```cmd
git push origin add-paddle
```

The first time you push a new branch, Git may ask for your GitHub username and password. If GitHub asks for a password, use a **Personal Access Token** instead — GitHub stopped accepting plain passwords. You can create one at: **https://github.com/settings/tokens** (select the `repo` scope).

### Open a Pull Request

Once your branch is pushed:

1. Go to the original project on GitHub (not your fork)
2. GitHub will usually show a yellow banner saying your branch was recently pushed — click **"Compare & pull request"**
3. Add a title and description explaining what you changed and why
4. Click **"Create pull request"**

The project owner can then review your changes, leave comments, and merge them in when they're ready.

### Keeping Your Fork Up to Date

If the original project gets new changes, you'll want to bring them into your fork. Do this once to connect the original:

```cmd
git remote add upstream https://github.com/original-owner/py-breakout.git
```

Then whenever you want to sync:

```cmd
git checkout main
git fetch upstream
git merge upstream/main
git push origin main
```

### Quick Reference

| Command                       | What it does                          |
|-------------------------------|---------------------------------------|
| `git status`                  | Show what files have changed          |
| `git diff`                    | Show the actual line changes          |
| `git checkout -b branch-name` | Create and switch to a new branch     |
| `git add .`                   | Stage all changed files               |
| `git commit -m "message"`     | Save a snapshot with a description    |
| `git push origin branch-name` | Upload your branch to GitHub          |
| `git pull`                    | Download and apply the latest changes |
| `git log --oneline`           | See a compact history of commits      |

---

## What's Next

Once Hello World is working, the next steps toward a real Breakout game will be:

- Drawing a paddle at the bottom of the screen
- Drawing a ball and making it move
- Bouncing the ball off the walls and paddle
- Adding rows of bricks to break
- Keeping score
