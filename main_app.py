import tkinter as tk
import json
from wifi_login import login

def logger():
    creds = json.load(open("creds.json"))
    username,password = creds["username"], creds["password"]

    login(username,password)

def change(usr,passw):
    with open("creds.json","r") as f:
        creds=json.load(f)

    creds["username"]=usr
    creds["password"]=passw
    
    with open("creds.json","w") as f:
        json.dump(creds,f,indent=4)


window = tk.Tk()
window.title("Wifi Loginer")
window.geometry("300x150")

label =tk.Label(
    master=window,
    text="Login to Wifi",
    font=("Arial",15)
)
label.pack(pady=40)

button =tk.Button(
    master=window,
    text ="Login Now",
    font=("Arial",20),
    command=logger
)
button.pack(pady=40)

def create_popup():
    changecred_window =tk.Toplevel()
    changecred_window.title("Change Credentials")

    username_entry=tk.Entry(
    master=changecred_window,
    font=("arial",20),
    )
    username_entry.pack(pady=40)
    
    password_entry=tk.Entry(
    master=changecred_window,
    font=("arial",20),
    )
    password_entry.pack(pady=40)

    button =tk.Button(
    master=changecred_window,
    text ="Change",
    font=("Arial",20),
    command=lambda: [change(username_entry.get(), password_entry.get()), changecred_window.destroy()]
    )
    button.pack(pady=40)

button =tk.Button(
    master=window,
    text ="Change Credentials",
    font=("Arial",20),
    command=create_popup
    )
button.pack(pady=40)





window.mainloop()
