import tkinter as tk

class AppointmentBookingWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Appointment Booking")
        self.root.geometry("350x400")

        # Patient Name
        tk.Label(self.root, text="Patient Name:").pack(pady=5)
        self.patient_name_entry = tk.Entry(self.root, width=30)
        self.patient_name_entry.pack()

        # Doctor Name
        tk.Label(self.root, text="Doctor Name:").pack(pady=5)
        self.doctor_name_entry = tk.Entry(self.root, width=30)
        self.doctor_name_entry.pack()

        # Appointment Date (YYYY-MM-DD)
        tk.Label(self.root, text="Appointment Date (YYYY-MM-DD):").pack(pady=5)
        self.date_entry = tk.Entry(self.root, width=30)
        self.date_entry.pack()

        # Appointment Time (HH:MM)
        tk.Label(self.root, text="Appointment Time (HH:MM):").pack(pady=5)
        self.time_entry = tk.Entry(self.root, width=30)
        self.time_entry.pack()

        # Message label for errors/success
        self.message_label = tk.Label(self.root, text="", fg="red")
        self.message_label.pack(pady=10)

        # Submit button
        tk.Button(self.root, text="Book Appointment", command=self.submit).pack(pady=15)

    def submit(self):
        self.message_label.config(text="", fg="red")

        patient_name = self.patient_name_entry.get()
        doctor_name = self.doctor_name_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()

        # Simple validation
        if not patient_name or not doctor_name or not date or not time:
            self.message_label.config(text="Please fill in all fields.", fg="red")
            return

        # You can add more validation for date/time format if you want

        self.message_label.config(text=f"Appointment for {patient_name} booked with Dr. {doctor_name} on {date} at {time}.", fg="green")

        # Clear fields
        self.patient_name_entry.delete(0, tk.END)
        self.doctor_name_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)

    def run(self):
        self.root.mainloop()
