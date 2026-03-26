# Markdown Guide

Markdown is a simple way to format text. Instead of clicking buttons like in Word, you add small symbols to your text and they control how it looks. GitHub, VS Code, PyCharm, and most coding tools understand Markdown and display it beautifully.

All the `.md` files in this project — including this one — are written in Markdown. You're reading formatted Markdown right now.

---

## Headings

Put one or more `#` symbols at the start of a line to make a heading. More `#` symbols = smaller heading.

```
# Big Heading
## Medium Heading
### Smaller Heading
#### Even Smaller
```

Renders as:

# Big Heading
## Medium Heading
### Smaller Heading
#### Even Smaller

---

## Bold and Italic

Wrap text in `**double asterisks**` for **bold**, or `*single asterisks*` for *italic*. Combine them with `***triple***` for ***bold italic***.

```
**bold**
*italic*
***bold italic***
```

---

## Lists

### Bullet lists

Start each line with `-` or `*`:

```
- First item
- Second item
- Third item
```

Renders as:

- First item
- Second item
- Third item

### Numbered lists

Start each line with a number and a period:

```
1. First step
2. Second step
3. Third step
```

Renders as:

1. First step
2. Second step
3. Third step

### Nested lists

Indent with two spaces to create a sub-list:

```
- Animals
  - Dogs
  - Cats
- Plants
  - Trees
  - Flowers
```

Renders as:

- Animals
  - Dogs
  - Cats
- Plants
  - Trees
  - Flowers

---

## Code

### Inline code

Wrap short snippets in single backticks to show them as `code`. Use this for file names, variable names, and short commands mentioned inside a sentence.

```
Run the `breakout` command to start the game.
```

Renders as:

Run the `breakout` command to start the game.

### Code blocks

For multiple lines of code, use three backticks before and after. Add the language name after the opening backticks for syntax highlighting:

````
```python
def main():
    BreakoutGame()
    arcade.run()
```
````

Renders as:

```python
def main():
    BreakoutGame()
    arcade.run()
```

Common language labels: `python`, `powershell`, `cmd`, `bash`, `html`, `json`.

---

## Links

```
[text to display](https://www.example.com)
```

For example:

```
[Python Downloads](https://www.python.org/downloads/)
```

Renders as:

[Python Downloads](https://www.python.org/downloads/)

---

## Images

Similar to links but with a `!` in front. The text in brackets is the "alt text" — a description shown if the image can't load:

```
![alt text](path/to/image.png)
```

---

## Tables

Use pipes `|` to separate columns and hyphens `---` to create the header row:

```
| Name    | Age | Favourite Language |
|---------|-----|--------------------|
| Richard | 14  | Python             |
| Tim     | 14  | Python             |
```

Renders as:

| Name    | Age | Favourite Language |
|---------|-----|--------------------|
| Richard | 14  | Python             |
| Tim     | 14  | Python             |

---

## Blockquotes

Start a line with `>` to create a callout or quote. Good for tips and warnings:

```
> **Tip:** Always activate your virtual environment before running the project.
```

Renders as:

> **Tip:** Always activate your virtual environment before running the project.

---

## Horizontal Rules

Three hyphens `---` on their own line creates a dividing line:

```
---
```

Renders as:

---

## Checkboxes

GitHub supports task lists using `- [ ]` for an unchecked box and `- [x]` for a checked one:

```
- [x] Install Python
- [x] Set up virtual environment
- [ ] Draw the paddle
- [ ] Add the ball
```

Renders as:

- [x] Install Python
- [x] Set up virtual environment
- [ ] Draw the paddle
- [ ] Add the ball

---

## Escaping Symbols

If you want to display a symbol like `*` or `#` without Markdown treating it as formatting, put a backslash `\` in front of it:

```
\*this is not italic\*
```

Renders as:

\*this is not italic\*

---

## Quick Reference

| Format | Syntax |
|---|---|
| Bold | `**text**` |
| Italic | `*text*` |
| Bold italic | `***text***` |
| Heading 1 | `# Heading` |
| Heading 2 | `## Heading` |
| Bullet list | `- item` |
| Numbered list | `1. item` |
| Inline code | `` `code` `` |
| Code block | ` ```python ` |
| Link | `[text](url)` |
| Image | `![alt](path)` |
| Blockquote | `> text` |
| Horizontal rule | `---` |
| Checkbox | `- [ ] item` |

---

## Previewing Markdown

You don't have to guess what your Markdown will look like — both VS Code and PyCharm can show you a live preview.

**VS Code:** Open a `.md` file, then press `Ctrl + Shift + V` to open a preview panel. Or click the preview icon in the top-right corner of the editor.

**PyCharm:** Open a `.md` file and click the **Preview** tab that appears at the bottom of the editor.

**GitHub:** Any `.md` file stored on GitHub is automatically rendered when you view it in a browser — no extra steps needed.
