import tkinter as tk
from tkinter import messagebox

app = tk.Tk() # create GUI App
app.title("Presh Login App")
app.geometry("1080x550+100+100")
app.resizable(False, False)

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showwarning("Input Error", "Please enter both username and password")
    else:
        messagebox.showinfo("Login Info", f"Username: {username}\nPassword: {password}")

# username label and entry
username_label = tk.Label(app, text="Username")
username_label.pack(pady=(15,5))

username_entry = tk.Entry(app, width=30)
username_entry.pack()

# password label and entry
password_label = tk.Label(app, text="Password")
password_label.pack(pady=(10,5))

password_entry = tk.Entry(app, width=30, show="*")
password_entry.pack()

# login button
login_button = tk.Button(app, text="Login", width=15, command=login)
login_button.pack(pady=15)


# Run the App
app.mainloop()