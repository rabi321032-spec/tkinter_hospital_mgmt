import tkinter as tk

class DoctorManagementWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Doctor Management")
        self.root.geometry("350x400")

        # Doctor Name
        tk.Label(self.root, text="Doctor Name:").pack(pady=5)
        self.name_entry = tk.Entry(self.root, width=30)
        self.name_entry.pack()

        # Specialty
        tk.Label(self.root, text="Specialty:").pack(pady=5)
        self.specialty_entry = tk.Entry(self.root, width=30)
        self.specialty_entry.pack()

        # Contact Number
        tk.Label(self.root, text="Contact Number:").pack(pady=5)
        self.contact_entry = tk.Entry(self.root, width=30)
        self.contact_entry.pack()

        # Email
        tk.Label(self.root, text="Email:").pack(pady=5)
        self.email_entry = tk.Entry(self.root, width=30)
        self.email_entry.pack()

        # Message label for errors/success
        self.message_label = tk.Label(self.root, text="", fg="red")
        self.message_label.pack(pady=10)

        # Submit button
        tk.Button(self.root, text="Submit", command=self.submit).pack(pady=15)

    def submit(self):
        # Clear previous message
        self.message_label.config(text="", fg="red")

        name = self.name_entry.get()
        specialty = self.specialty_entry.get()
        contact = self.contact_entry.get()
        email = self.email_entry.get()

        # Simple validation
        if name == "" or specialty == "" or contact == "" or email == "":
            self.message_label.config(text="Please fill in all fields.", fg="red")
            return

        self.message_label.config(text=f"Doctor '{name}' added successfully!", fg="green")

        # Clear fields after submit
        self.name_entry.delete(0, tk.END)
        self.specialty_entry.delete(0, tk.END)
        self.contact_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def run(self):
        self.root.mainloop()
