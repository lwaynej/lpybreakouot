# Git and GitHub Guide for Contributors

This document provides a structured introduction to installing Git, creating a GitHub account, and using a standard workflow to contribute changes to a project.

---

# 1. Installing Git

## Verify Installation

Open a terminal (Linux/macOS) or Git Bash / Command Prompt (Windows) and run:

```
git --version
```

If a version number is displayed, Git is already installed.

---

## macOS

Option 1 (recommended):
- Run `git --version` and follow the prompt to install Xcode Command Line Tools.

Option 2 (Homebrew):
```
brew install git
```

---

## Linux

### Ubuntu / Debian
```
sudo apt update
sudo apt install git
```

### Fedora
```
sudo dnf install git
```

---

## Windows

1. Download Git from:
   https://git-scm.com
2. Run the installer using default settings
3. Use **Git Bash** for command-line operations

---

# 2. Creating a GitHub Account

1. Navigate to https://github.com
2. Select **Sign up**
3. Provide a username, email address, and password
4. Complete verification

For more details please see the GitHub documentation
* [two-factor authentication](https://docs.github.com/en/get-started/onboarding/getting-started-with-your-github-account#4-configuring-two-factor-authentication)
---

# 3. Contribution Workflow Overview

The standard workflow used in this project:

```
Fork → Clone → Branch → Modify → Commit → Push → Pull Request
```

---

# 4. Step-by-Step Workflow

## 4.1 Fork the Repository

1. Navigate to the project repository on GitHub
2. Select **Fork** (top-right corner)

This creates a personal copy of the repository under your account.

---

## 4.2 Clone the Repository

Replace placeholders with your GitHub username and repository name:

```
git clone https://github.com/<your-username>/<repository>.git
cd <repository>
```

---

## 4.3 Create a Branch

Create a new branch for your changes:

```
git checkout -b <branch-name>
```

Use a descriptive branch name (e.g., `add-paddle-control`).

---

## 4.4 Modify the Code

Make the required changes using your editor or IDE. Save all modified files.

---

## 4.5 Commit Changes

Stage and commit your changes:

```
git add .
git commit -m "Brief description of changes"
```

Guidelines:
- Use concise, descriptive commit messages
- Commit logically related changes together

---

## 4.6 Push Changes

Push your branch to your GitHub repository:

```
git push origin <branch-name>
```
---

## 4.7 Open a Pull Request

1. Navigate to your repository on GitHub
2. Select **Compare & pull request**
3. Review your changes
4. Submit the pull request

---

# 5. Common Commands

```
git status          # View current changes
git add .           # Stage changes
git commit -m ""    # Commit changes
git push            # Push changes
git pull            # Retrieve updates
```

---

# 6. Troubleshooting

## No changes to commit
Ensure files have been modified and saved before running `git add`.

## Permission errors
Verify you are pushing to your fork, not the original repository.

## Git not recognized
Confirm Git is installed and available in your system PATH.

---

# 7. Summary

Typical contribution sequence:

```
git clone <repo>
git checkout -b <branch>
git add .
git commit -m "message"
git push
```

After pushing, complete the process by opening a pull request on GitHub.

# Appendix

## GitHub Authentication

Pushing to GitHub requires authentication. Using personal access token is the
currently recommended authentication. If you are logged into a GitHub, this URL
will take you to the page for generating tokens and selects the recommended
token options:

Here is the URL with line breaks for readability (not copy-pasteable)
```
https://github.com/settings/personal-access-tokens/new?name=Tutorial+Repo+Push+Token\
       &description=Used+to+push+changes+to+my+fork+for+the+Python+tutorial\
       &expires_in=30&contents=write
```
[Generate PAT](https://github.com/settings/personal-access-tokens/new?name=Tutorial+Repo+Push+Token&description=Used+to+push+changes+to+my+fork+for+the+Python+tutorial&expires_in=30&contents=write)

Scroll to the bottom of the page and click "Generate Token".  This will bring up a dialog box,
you must click "Generate Token" once more time. This will generate the token and allow you to
copy it. **Important**, this is the **only** time that you will be able to access this token. 
Do the remainder of these steps before closing this page.

In the command prompt (macOS):
```bash
git config --global credential.helper osxkeychain
printf "protocol=https\nhost=github.com\nusername=YOUR_USERNAME\npassword=YOUR_PAT\n\n" | git credential-osxkeychain store
```
Replace 'YOUR_USERNAME' with your GitHub username (usually your email address)
Copy and paste the PAT you just generated and paste it insead of 'YOUR_PAT'

This will allow you to use HTTPS to `clone`, `push`, and `pull` using git. 

More details can be found on GitHub's [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens?versionId=free-pro-team%40latest&productId=get-started&restPage=onboarding%2Cgetting-started-with-your-github-account)

### Trouble Shooting

Verify PAT:
```bash
printf "protocol=https\nhost=github.com\n\n" | git credential fill
```
Check protocol used for access:`
```bash
git remote -v
```
Check for URL rewrites
```bash
git config --global --get-regexp '^url\..*\.insteadof$'
```

Add trace to output (failing command)
```bash
GIT_TRACE=1 GIT_CURL_VERBOSE=1 git push
```
### Crendential Managers

Windows:
```bash
git config --global credential.helper manager
```

Linux:
```bash
git config --global credential.helper store
```
