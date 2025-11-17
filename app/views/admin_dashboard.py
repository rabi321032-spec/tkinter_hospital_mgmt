import tkinter as tk

class AdminDashboardWindow:
    def __init__(self, parent=None):
        self.parent = parent  # store reference to DashboardWindow
        self.root = tk.Tk()
        self.root.title("Admin Dashboard")
        self.root.geometry("350x300")

        tk.Label(self.root, text="Admin Dashboard", font=("Arial", 16)).pack(pady=20)

        # Other buttons...
        tk.Button(self.root, text="Back to Dashboard", width=25, command=self.back_to_dashboard).pack(pady=15)

    def back_to_dashboard(self):
        self.root.destroy()  # close admin dashboard
        if self.parent:
            self.parent.root.deiconify()  # show dashboard again

    def run(self):
        self.root.mainloop()
