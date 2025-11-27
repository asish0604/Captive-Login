# 📶 WiFi Login Manager

A beautiful GUI application to automatically login to captive portal WiFi networks with saved credentials.

## ✨ Features

- 🎨 Modern, sleek GUI interface
- 🔐 Secure credential storage
- ⚡ Quick login with keyboard shortcut
- 🔔 Desktop notifications on successful login
- 🖥️ Cross-platform (Windows & Linux)

## 📋 Prerequisites

- Python 3.7 or higher
- Internet connection
- Access to the WiFi network that requires login

## 🚀 Quick Start

### Step 1: Clone the Repository

```bash
git clone https://github.com/asish0604/Captive-Login.git
cd Captive-Login
```

### Step 2: Install Dependencies

```bash
pip install requests PyQt6
```

**What gets installed:**

- `requests` - For making HTTP requests to the login portal
- `PyQt6` - For the graphical user interface (includes PyQt6.QtWidgets, PyQt6.QtCore, PyQt6.QtGui)

**Built-in Python modules (no install needed):**

- `subprocess` - For running system commands and notifications
- `json` - For storing and reading credentials
- `sys` - For command-line arguments and system operations

### Step 3: Run the Application

```bash
python main.py
```

### Step 4: Setup Your Credentials

1. The GUI will open
2. Click **"⚙️ Change Credentials"**
3. Enter your WiFi username and password
4. Click **"Update Credentials"**
5. Click **"🚀 Login Now"** to connect!

That's it! Your credentials are saved for next time.

## 💻 Usage

### GUI Mode (Interactive)

Run the application with the graphical interface:

```bash
python main.py
```

This will open a window where you can:

- Click "Login Now" to connect
- Click "Change Credentials" to update your username/password

### Command Line Mode (Quick Login)

For quick login without GUI (perfect for scripts and shortcuts):

```bash
python main.py --login
```

or

```bash
python main.py -l
```

## ⚙️ Auto-Start Setup

### 🐧 Linux

**Get the full path to your script:**

```bash
pwd  # Copy this path, you'll need it below
```

#### Option 1: Keyboard Shortcut (Niri/Sway/i3)

For **Niri**, add to `~/.config/niri/config.kdl`:

```kdl
binds {
    Mod+Shift+W { spawn "sh" "-c" "cd /home/YOUR_USERNAME/Captive-Login && python main.py -l"; }
}
```

For **i3/Sway**, add to config:

```bash
bindsym $mod+Shift+w exec "cd /home/YOUR_USERNAME/Captive-Login && python main.py -l"
```

Replace `/home/YOUR_USERNAME/Captive-Login` with the path you copied above.

#### Option 2: Quick Alias

Add to `~/.bashrc` or `~/.zshrc`:

```bash
alias wifi-login="cd /home/YOUR_USERNAME/Captive-Login && python main.py -l"
```

Then reload: `source ~/.bashrc`

Now just type `wifi-login` in terminal!

#### Option 3: Desktop Entry

Create `~/.local/share/applications/wifi-login.desktop`:

```ini
[Desktop Entry]
Name=WiFi Login
Comment=Login to Captive Portal WiFi
Exec=sh -c "cd /home/YOUR_USERNAME/Captive-Login && python main.py"
Icon=network-wireless
Terminal=false
Type=Application
Categories=Network;Utility;
```

Replace the path with yours.

### 🪟 Windows

**Get the full path to your script:**

1. Open the folder in File Explorer
2. Click the address bar and copy the path (e.g., `C:\Users\YourName\Captive-Login`)

#### Option 1: Startup Folder (Auto-run on Login)

1. Press `Win + R` and type: `shell:startup`
2. Create `wifi-login.bat` in that folder
3. Edit it and add (replace path):
   ```batch
   @echo off
   cd C:\Users\YourName\Captive-Login
   python main.py -l
   ```
4. Save

Now auto-logins when Windows starts!

#### Option 2: Desktop Shortcut

1. Right-click Desktop → New → Shortcut
2. Enter:
   ```
   cmd /c "cd C:\Users\YourName\Captive-Login && python main.py"
   ```
3. Name it "WiFi Login"

#### Option 3: Keyboard Shortcut

1. Create desktop shortcut (see above)
2. Right-click → Properties
3. Click "Shortcut key" field
4. Press desired keys (e.g., `Ctrl + Alt + W`)
5. Click OK

## 🔔 Notifications

The script sends desktop notifications on successful login:

- **Linux**: Uses `notify-send` (pre-installed on most distros)
- **Windows**: Desktop notifications currently under development

If notifications don't work on Linux, install:

```bash
sudo apt install libnotify-bin  # Ubuntu/Debian
sudo pacman -S libnotify        # Arch Linux
```

## 🛠️ Troubleshooting

### "Module not found" error

```bash
pip install requests PyQt6
```

### Notification daemon conflict (Linux)

If using COSMIC/Noctalia and getting duplicate notifications:

```bash
killall mako
systemctl --user mask mako.service
```

### Can't connect to WiFi login page

- Make sure you're connected to the WiFi network first
- Check if the login URL in `wifi_login.py` matches your network
- The default URL is `http://10.10.10.2:8090/login.xml`

### Script doesn't auto-start

- **Linux**: Check file paths in your config files
- **Windows**: Verify Python is in your PATH (`python --version` in cmd)

## 📁 File Structure

```
Captive-Login/
├── main.py           # Main GUI application
├── wifi_login.py     # Login logic
├── creds.json        # Your credentials (you create this)
└── README.md         # This file
```

## 🔒 Security Notes

- `creds.json` stores credentials in plain text
- Keep this file secure and don't share it
- Don't commit `creds.json` to version control
- Consider setting file permissions: `chmod 600 creds.json` (Linux)

## 📝 License

Free to use and modify for personal use.

## 🤝 Contributing

Feel free to submit issues or pull requests!

---

**Made with ❤️ for easier WiFi logins**
