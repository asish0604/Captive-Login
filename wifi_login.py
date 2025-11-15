import requests


def login(username, password):
    # Login URL
    login_url = "http://10.10.10.2:8090/login.xml"

    # Form data
    payload = {
        "mode": "191",
        "username": username,
        "password": password,
        "a": "1738391626450",
        "producttype": "0",
    }

    # Headers
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "http://10.10.10.2:8090",
        "Referer": "http://10.10.10.2:8090/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)",
    }

    session = requests.Session()

    try:
        # Send POST request with a timeout
        response = session.post(login_url, data=payload, headers=headers, timeout=5)

        if response.status_code == 200:
            if "success" in response.text.lower():
                print("Wifi Login successful!")
                return True
            else:
                print("Wifi Login failed!")
                print(response.text)
                return False
        else:
            print(f"Server returned status code: {response.status_code}")
            return False

    except requests.exceptions.Timeout:
        print("Connection timed out! The login server didn’t respond.")
        return False

    except requests.exceptions.ConnectionError:
        print("Network error! Check if you're connected to the correct Wi-Fi.")
        return False

    except requests.exceptions.RequestException as e:
        print(f"An unexpected error occurred: {e}")
        return False
