import tkinter as tk

class MedicalRecordsWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Medical Records")
        self.root.geometry("400x450")

        # Patient Name
        tk.Label(self.root, text="Patient Name:").pack(pady=5)
        self.patient_name_entry = tk.Entry(self.root, width=35)
        self.patient_name_entry.pack()

        # Record Date (YYYY-MM-DD)
        tk.Label(self.root, text="Record Date (YYYY-MM-DD):").pack(pady=5)
        self.record_date_entry = tk.Entry(self.root, width=35)
        self.record_date_entry.pack()

        # Diagnosis
        tk.Label(self.root, text="Diagnosis:").pack(pady=5)
        self.diagnosis_entry = tk.Entry(self.root, width=35)
        self.diagnosis_entry.pack()

        # Prescriptions
        tk.Label(self.root, text="Prescriptions:").pack(pady=5)
        self.prescriptions_entry = tk.Entry(self.root, width=35)
        self.prescriptions_entry.pack()

        # Notes
        tk.Label(self.root, text="Additional Notes:").pack(pady=5)
        self.notes_text = tk.Text(self.root, width=40, height=5)
        self.notes_text.pack()

        # Message label for errors/success
        self.message_label = tk.Label(self.root, text="", fg="red")
        self.message_label.pack(pady=10)

        # Submit button
        tk.Button(self.root, text="Save Record", command=self.submit).pack(pady=15)

    def submit(self):
        self.message_label.config(text="", fg="red")

        patient_name = self.patient_name_entry.get()
        record_date = self.record_date_entry.get()
        diagnosis = self.diagnosis_entry.get()
        prescriptions = self.prescriptions_entry.get()
        notes = self.notes_text.get("1.0", tk.END).strip()

        # Simple validation
        if not patient_name or not record_date or not diagnosis or not prescriptions:
            self.message_label.config(text="Please fill in all required fields.", fg="red")
            return

        self.message_label.config(text=f"Medical record for '{patient_name}' saved successfully!", fg="green")

        # Clear fields after submission
        self.patient_name_entry.delete(0, tk.END)
        self.record_date_entry.delete(0, tk.END)
        self.diagnosis_entry.delete(0, tk.END)
        self.prescriptions_entry.delete(0, tk.END)
        self.notes_text.delete("1.0", tk.END)

    def run(self):
        self.root.mainloop()
