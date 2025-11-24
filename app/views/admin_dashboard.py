import tkinter as tk

class AdminDashboardWindow:
    def __init__(self, parent=None):
        self.parent = parent  # reference to DashboardWindow
        self.root = tk.Tk()
        self.root.title("Admin Dashboard")
        self.root.geometry("350x300")

        tk.Label(self.root, text="Admin Dashboard", font=("Arial", 16)).pack(pady=20)

        # Your existing admin buttons
        tk.Button(self.root, text="User Management", width=25).pack(pady=8)
        tk.Button(self.root, text="System Settings", width=25).pack(pady=8)
        tk.Button(self.root, text="Reports", width=25).pack(pady=8)
        tk.Button(self.root, text="Logs", width=25).pack(pady=8)

        # Back to Dashboard button
        tk.Button(self.root, text="Back to Dashboard", width=25, command=self.back_to_dashboard).pack(pady=15)

    def back_to_dashboard(self):
        self.root.destroy()  # close admin dashboard
        if self.parent:
            self.parent.root.deiconify()  # show dashboard again

    def run(self):
        self.root.mainloop()
