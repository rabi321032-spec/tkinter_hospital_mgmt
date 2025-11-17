import tkinter as tk
from tkinter import messagebox

from app.model.login_model import LoginModel
from app.services.login_services import LoginService

class LoginWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Login")
        self.root.geometry("300x180")
        self.login_success = False  # flag for login status

        tk.Label(self.root, text="Username").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        tk.Label(self.root, text="Password").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        # Error message label (initially empty)
        self.error_label = tk.Label(self.root, text="", fg="red")
        self.error_label.pack()

        tk.Button(self.root, text="Login", command=self.login).pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        model = LoginModel(username, password)
        service = LoginService()
        result = service.authenticate(model)

        if result:
            self.login_success = True
            self.root.destroy()  # close login window
        else:
            # Show error message inside the window in red
            self.error_label.config(text="Wrong credentials. Please try again.")

    def run(self):
        self.root.mainloop()
        return self.login_success
