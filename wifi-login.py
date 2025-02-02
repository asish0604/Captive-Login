import requests

# Login URL
login_url = "http://10.10.10.2:8090/login.xml"

# Form data (replace with your actual credentials)
payload = {
    "mode": "191",
<<<<<<< HEAD
    "username": "Your_Username,  # Your college username
    "password": "Your-Password",  # Your password
=======
    "username": "YOUR_USERNAME",  # Your college username
    "password": "YOUR_PASSWORD",  # Your password
>>>>>>> 8863dc4 (Made the code for public use removing personal info)
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
