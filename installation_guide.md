# Installation Guide

## Prerequisites

- Python 3.7+ installed
- Terminal access
- Text editor 

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

## Step 2: Create Virtual Environment

```bash
python3 -m venv venv
```

> **Note:** If `python3` doesn't work, try `python` or `py` depending on your Python installation.

## Step 3: Activate Virtual Environment

### Linux:
```bash
source venv/bin/activate
```

### Windows:

**Option A - Command Prompt:**
```cmd
venv\Scripts\activate
```

**Option B - PowerShell:**
```powershell
venv\Scripts\Activate.ps1
```

If PowerShell gives execution policy error:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Run this first, then try activation again.

### Successful activation indicators:
Your prompt should show `(venv)` at the beginning.

**Example:** `(venv) C:\Desktop\flask_upload_app>`

## Step 4: Install Dependencies

```bash
pip install Flask
pip install -r requirements.txt
```

## Step 5: Run the Application

```bash
python app.py
```

Visit `http://<your-localhost-IP>:1212`

You'll see output like:
```
* Running on http://127.0.0.1:1212
* Running on http://[your-local-ip]:1212
```

## Step 6: Stop the Server

When finished, in the terminal press:
```
Ctrl + C
```

## ⚠️ WARNING

I never tried setting up the Cloud server on Windows machine!
So if you have some error check `windows-error.md`, might help.
