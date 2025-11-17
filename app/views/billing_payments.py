import tkinter as tk

class BillingPaymentsWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Billing & Payments")
        self.root.geometry("400x400")

        # Patient Name
        tk.Label(self.root, text="Patient Name:").pack(pady=5)
        self.patient_name_entry = tk.Entry(self.root, width=35)
        self.patient_name_entry.pack()

        # Billing Date (YYYY-MM-DD)
        tk.Label(self.root, text="Billing Date (YYYY-MM-DD):").pack(pady=5)
        self.billing_date_entry = tk.Entry(self.root, width=35)
        self.billing_date_entry.pack()

        # Amount
        tk.Label(self.root, text="Amount:").pack(pady=5)
        self.amount_entry = tk.Entry(self.root, width=35)
        self.amount_entry.pack()

        # Payment Method
        tk.Label(self.root, text="Payment Method:").pack(pady=5)
        self.payment_method_entry = tk.Entry(self.root, width=35)
        self.payment_method_entry.pack()

        # Message label for errors/success
        self.message_label = tk.Label(self.root, text="", fg="red")
        self.message_label.pack(pady=10)

        # Submit button
        tk.Button(self.root, text="Process Payment", command=self.submit).pack(pady=15)

    def submit(self):
        self.message_label.config(text="", fg="red")

        patient_name = self.patient_name_entry.get()
        billing_date = self.billing_date_entry.get()
        amount = self.amount_entry.get()
        payment_method = self.payment_method_entry.get()

        # Simple validation
        if not patient_name or not billing_date or not amount or not payment_method:
            self.message_label.config(text="Please fill in all fields.", fg="red")
            return

        # Optionally, you can validate amount is numeric

        self.message_label.config(text=f"Payment of {amount} processed for {patient_name}.", fg="green")

        # Clear fields after submission
        self.patient_name_entry.delete(0, tk.END)
        self.billing_date_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.payment_method_entry.delete(0, tk.END)

    def run(self):
        self.root.mainloop()
