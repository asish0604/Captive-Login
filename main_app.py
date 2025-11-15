import customtkinter as ctk
import json
from wifi_login import login
import sys


def logger():
    creds = json.load(open("creds.json"))
    username, password = creds["username"], creds["password"]
    login(username, password)


if "-l" in sys.argv or "--login" in sys.argv:
    logger()
    sys.exit(0)


def change(usr, passw):
    with open("creds.json", "r") as f:
        creds = json.load(f)
    creds["username"] = usr
    creds["password"] = passw
    with open("creds.json", "w") as f:
        json.dump(creds, f, indent=4)


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

window = ctk.CTk()
window.title("Wifi Loginer")
window.geometry("400x350")
window.resizable(False, False)


label = ctk.CTkLabel(
    master=window,
    text="Login to Wifi",
    font=ctk.CTkFont(size=24, weight="bold"),
    text_color="#EAEAEA",
)
label.pack(pady=(40, 20))


button_login = ctk.CTkButton(
    master=window,
    text="Login Now",
    font=ctk.CTkFont(size=18, weight="bold"),
    height=45,
    width=200,
    corner_radius=12,
    command=logger,
)
button_login.pack(pady=10)


def create_popup():
    changecred_window = ctk.CTkToplevel()
    changecred_window.title("Change Credentials")
    changecred_window.geometry("350x300")
    changecred_window.resizable(False, False)

    title_label = ctk.CTkLabel(
        master=changecred_window,
        text="Update Credentials",
        font=ctk.CTkFont(size=20, weight="bold"),
    )
    title_label.pack(pady=(25, 10))

    username_entry = ctk.CTkEntry(
        master=changecred_window,
        placeholder_text="Enter Username",
        width=250,
        height=40,
        font=ctk.CTkFont(size=16),
    )
    username_entry.pack(pady=(10, 10))

    password_entry = ctk.CTkEntry(
        master=changecred_window,
        placeholder_text="Enter Password",
        width=250,
        height=40,
        font=ctk.CTkFont(size=16),
        show="*",
    )
    password_entry.pack(pady=(10, 20))

    button = ctk.CTkButton(
        master=changecred_window,
        text="Change",
        font=ctk.CTkFont(size=16, weight="bold"),
        height=40,
        width=150,
        corner_radius=10,
        command=lambda: [
            change(username_entry.get(), password_entry.get()),
            changecred_window.destroy(),
        ],
    )
    button.pack(pady=10)


button_change = ctk.CTkButton(
    master=window,
    text="Change Credentials",
    font=ctk.CTkFont(size=18, weight="bold"),
    height=45,
    width=220,
    corner_radius=12,
    fg_color="#2C74B3",
    command=create_popup,
)
button_change.pack(pady=20)

window.mainloop()
