from app.views.login_window import LoginWindow
from app.views.dashboard_window import DashboardWindow
import tkinter as tk
from tkinter import messagebox

def main():
    login_window = LoginWindow()
    success = login_window.run()

    if success:
        dashboard = DashboardWindow()
        dashboard.run()
    else:
        # No need to show error here anymore since login window handles it
        pass

if __name__ == "__main__":
    main()
