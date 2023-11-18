# Download the latest Python installer
$url = "https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe" # Replace with the latest Python version URL
$output = "$env:TEMP\python-3.10.0-amd64.exe" # Replace with the desired version
Invoke-WebRequest -Uri $url -OutFile $output

# Install Python
Start-Process -Wait -FilePath $output -ArgumentList "/quiet", "InstallAllUsers=1", "PrependPath=1"
Remove-Item $output

# Add Python to PATH
$pythonPath = Join-Path $env:ProgramFiles 'Python\Python310'
$env:Path += ";$pythonPath;$pythonPath\Scripts"

# Install required Python packages using pip
cmd /c 'C:\Program Files\Python310\python.exe' -m pip install pyautogui pillow opencv-python