<<<<<<< HEAD
# Captive-Login
Script to login to captive portal of Wifi

# WiFi Captive Portal Login Script

Welcome to the WiFi Captive Portal Login Script! This script automates the login process for a WiFi captive portal, saving you time and hassle. 🚀

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.x
- `requests` library (install using `pip install requests`)

## 🚀 Getting Started

### 1. Clone the Repository

First, clone the repository to your local machine:
```sh
git clone https://github.com/yourusername/wifi-login.git
cd wifi-login
```

### 2. Replace Credentials

Open the wifi-login.py file and replace YOUR_USERNAME and YOUR_PASSWORD with your actual username and password:

```python
import requests

# Login URL
login_url = "http://10.10.10.2:8090/login.xml"

# Form data (replace with your actual credentials)
payload = {
    "mode": "191",
    "username": "YOUR_USERNAME",  # Your college username
    "password": "YOUR_PASSWORD",  # Your password
    "a": "1738391626450",  # Dynamic value (may need updating)
    "producttype": "0"
}

# Headers (copied from the request)
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "http://10.10.10.2:8090",
    "Referer": "http://10.10.10.2:8090/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
}

# Create a session
session = requests.Session()

# Send the POST request
response = session.post(login_url, data=payload, headers=headers)

# Check if login was successful
if response.status_code == 200 and "success" in response.text.lower():
    print("Login successful!")
else:
    print("Login failed!")
    print(response.text)  # Print the response to debug
```
3. Get Dynamic Values
To get the dynamic values required for the script:

Open your browser and navigate to the login page.
Right-click on the page and select "Inspect" or press Ctrl+Shift+I to open the developer tools.
Go to the "Network" tab and perform a login attempt.
Find the login request and inspect the form data to get the dynamic values (e.g., a).
4. Run the Script
Run the script using the following command:

python wifi-login.py

🖥️ Automate on Windows
1. Create a Batch File
Open Notepad and paste the following content:
```markdown
@echo off
python C:\path\to\wifi-login.py
```
Save the file as wifi-login.bat.

2. Move the Batch File to the Startup Folder
Move wifi-login.bat to C:\Users\asish\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\.

🐧 Automate on Unix/Linux
1. Create a Shell Script
Open a terminal and create a new file:

nano wifi-login.sh

Paste the following content:
#!/bin/bash
python3 /path/to/wifi-login.py

Save and close the file.

2. Make the Script Executable
Make the script executable:

chmod +x wifi-login.sh

3. Add the Script to Startup
Open the crontab editor:

crontab -e

Add the following line to run the script at startup:

@reboot /path/to/wifi-login.sh

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

📞 Contact
For any issues or questions, please open an issue on GitHub.

=======
>>>>>>> 8863dc4 (Made the code for public use removing personal info)
