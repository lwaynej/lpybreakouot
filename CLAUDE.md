# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

A collaborative breakout/brick-breaker game in Python, developed cross-platform between macOS and Windows users.

## Environment Setup

**macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

**Windows (PowerShell):**
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

If PowerShell blocks activation: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

## Library Options

| Library | Install | Notes |
|---------|---------|-------|
| Tkinter | built-in | No install needed; Canvas-based drawing |
| Turtle | built-in | No install needed; vector graphics |
| Pygame | `pip install pygame-ce` | Classic game loop; many tutorials available |
| Arcade | `pip install arcade` | Modern OOP structure; `on_draw`/`on_update` pattern |

**Suggested progression:** Tkinter → Arcade (or Pygame as alternative)

## Install and Run

Install the package in editable mode (do this once after setting up the venv):
```bash
pip install -e .
```

Then run the game:
```bash
breakout
```

Or directly:
```bash
python -m breakout.main
```

## Syncing Between Machines

After installing dependencies:
```bash
python -m pip freeze > requirements.txt
# Collaborator installs with:
python -m pip install -r requirements.txt
```

## Architecture Notes

- **Pygame** uses a manual game loop: poll events → update state → draw → `clock.tick(60)`
- **Arcade** uses a class-based pattern inheriting from `arcade.Window`, with `on_update(delta_time)` and `on_draw()` callbacks — no manual loop needed
- For a breakout game, key concepts to implement: game loop, paddle/ball/brick state, collision detection, and keyboard event handling
