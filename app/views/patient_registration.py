import tkinter as tk

class PatientRegistrationWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Patient Registration")
        self.root.geometry("350x400")

        # Patient Name
        tk.Label(self.root, text="Patient Name:").pack(pady=5)
        self.name_entry = tk.Entry(self.root, width=30)
        self.name_entry.pack()

        # Age
        tk.Label(self.root, text="Age:").pack(pady=5)
        self.age_entry = tk.Entry(self.root, width=30)
        self.age_entry.pack()

        # Gender
        tk.Label(self.root, text="Gender:").pack(pady=5)
        self.gender_entry = tk.Entry(self.root, width=30)
        self.gender_entry.pack()

        # Contact Number
        tk.Label(self.root, text="Contact Number:").pack(pady=5)
        self.contact_entry = tk.Entry(self.root, width=30)
        self.contact_entry.pack()

        # Address
        tk.Label(self.root, text="Address:").pack(pady=5)
        self.address_entry = tk.Entry(self.root, width=30)
        self.address_entry.pack()

        # Label to show error or success messages
        self.message_label = tk.Label(self.root, text="", fg="red")
        self.message_label.pack(pady=10)

        # Submit button
        tk.Button(self.root, text="Submit", command=self.submit).pack(pady=15)

    def submit(self):
        # Clear previous message
        self.message_label.config(text="", fg="red")

        # Get all entered data
        name = self.name_entry.get()
        age = self.age_entry.get()
        gender = self.gender_entry.get()
        contact = self.contact_entry.get()
        address = self.address_entry.get()

        # Simple validation: check for empty fields
        if name == "" or age == "" or gender == "" or contact == "" or address == "":
            self.message_label.config(text="Please fill in all fields.", fg="red")
            return

        # Show success message
        self.message_label.config(text=f"Patient '{name}' registered successfully!", fg="green")

        # Clear fields after submission
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.gender_entry.delete(0, tk.END)
        self.contact_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def run(self):
        self.root.mainloop()
