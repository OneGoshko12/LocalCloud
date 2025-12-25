# Installation Guide

## Prerequisites

- Python 3.7+ installed
- Terminal access
- Text editor 
- uv (package manager) --> ( see Step 2, if you don't have it)

**For Windows:**
- VS Code, Notepad++, etc.

**For Linux:**
- nano, vim, gedit, VS Code, or any preferred editor

## Step 1: Clone the Repository

```bash
cd Desktop   # (or wherever you want to download it)
git clone https://github.com/OneGoshko12/LocalCloud.git
cd LocalCloud
cd flask_upload_app
```

## Step 2: Install uv ( if you don't already have it)

### Linux:
Run this in your terminal (it's the official standalone installer for Linux):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
This downloads and installs *uv* to ~/.local/bin/uv.
It should automatically handle adding it to your PATH, but if you're using fish shell, you might need to restart your terminal (close and reopen) for it to take effect.

### Windows:
Run this in your PowerShell or Command Prompt (cmd) - (it's the official standalone installer for Windows):
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
This downloads and installs uv to %USERPROFILE%\.cargo\bin\.
It should automatically handle adding it to your PATH, but you might need to restart your terminal (close and reopen) for it to take effect.

### Alternative methods:
If you have Winget installed, run: 
```
winget install --id=astral-sh.uv -e
```
Or with Scoop: 
```
scoop install main/uv
```

## Step 3: Install dependencies

```
uv sync
```

## Step 4: Run the Application

```bash
uv run python app.py
#or
uv run app.py
```

Visit `http://<your-localhost-IP>:1212`

You'll see output like:
```
* Running on http://127.0.0.1:1212
* Running on http://[your-local-ip]:1212
```

## Step 5: Stop the Server

When finished, in the terminal press:
```
Ctrl + C
```

## ⚠️ WARNING

I never tried setting up the Cloud server on Windows machine!
So if you have some error check `windows-error.md`, might help.
