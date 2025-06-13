# Windows-Specific Troubleshooting

## Windows Defender/Antivirus

- Your antivirus might flag the Python server
- Add an exception for your project folder if needed

Set it up from here:
![Windows Defender/Antivirus](screenshots/screenshot-2025-06-13-04.png)

## Port Issues

If port 1212 is in use, you can change it in `app.py` on this line:

```python
app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)  # Use port 8080 instead, or any port you like
```

## "python is not recognized"

- Add Python to your PATH environment variable
- Try `py` or `python3` instead of `python`

## "pip is not recognized"

- Usually installs with Python, try:
  ```bash
  py -m pip
  ```

## Virtual Environment Won't Activate

Try the full path:

### Command Prompt:
```cmd
C:\Users\user\Desktop\LocalCloud\flask_upload_app\venv\Scripts\activate
```

### PowerShell:
```powershell
C:\Users\user\Desktop\LocalCloud\flask_upload_app\venv\Scripts\Activate.ps1
```

If PowerShell gives execution policy error:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Run this first, then try activation again.

### Successful activation indicators:
Your prompt should show `(venv)` at the beginning.

**Example:** `(venv) C:\Desktop\flask_upload_app>`

## Permission Errors

- Run Command Prompt as Administrator
- Or use PowerShell with execution policy change (shown above):
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```