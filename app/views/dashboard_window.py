import tkinter as tk

class DashboardWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Dashboard")
        self.root.geometry("300x450")

        tk.Label(self.root, text="Welcome to Dashboard", font=("Arial", 14)).pack(pady=20)

        tk.Button(self.root, text="Patient Registration", width=20, command=self.open_patient_registration).pack(pady=5)
        tk.Button(self.root, text="Doctor Management", width=20, command=self.open_doctor_management).pack(pady=5)
        tk.Button(self.root, text="Appointment Booking", width=20, command=self.open_appointment_booking).pack(pady=5)
        tk.Button(self.root, text="Medical Records", width=20, command=self.open_medical_records).pack(pady=5)
        tk.Button(self.root, text="Billing & Payments", width=20, command=self.open_billing_payments).pack(pady=5)
        tk.Button(self.root, text="Admin Dashboard", width=20, command=self.open_admin_dashboard).pack(pady=5)

    def open_patient_registration(self):
        self.root.withdraw()
        from app.views.patient_registration import PatientRegistrationWindow

        def on_close():
            self.root.deiconify()
            patient_reg_window.root.destroy()

        patient_reg_window = PatientRegistrationWindow()
        patient_reg_window.root.protocol("WM_DELETE_WINDOW", on_close)
        patient_reg_window.run()

    def open_doctor_management(self):
        self.root.destroy()
        from app.views.doctor_management import DoctorManagementWindow
        doctor_mgmt_window = DoctorManagementWindow()
        doctor_mgmt_window.run()

    def open_appointment_booking(self):
        self.root.withdraw()
        from app.views.appointment_booking import AppointmentBookingWindow

        def on_close():
            self.root.deiconify()
            appointment_window.root.destroy()

        appointment_window = AppointmentBookingWindow()
        appointment_window.root.protocol("WM_DELETE_WINDOW", on_close)
        appointment_window.run()

    def open_medical_records(self):
        self.root.withdraw()
        from app.views.medical_records import MedicalRecordsWindow

        def on_close():
            self.root.deiconify()
            medical_records_window.root.destroy()

        medical_records_window = MedicalRecordsWindow()
        medical_records_window.root.protocol("WM_DELETE_WINDOW", on_close)
        medical_records_window.run()

    def open_billing_payments(self):
        self.root.withdraw()
        from app.views.billing_payments import BillingPaymentsWindow

        def on_close():
            self.root.deiconify()
            billing_window.root.destroy()

        billing_window = BillingPaymentsWindow()
        billing_window.root.protocol("WM_DELETE_WINDOW", on_close)
        billing_window.run()

    def open_admin_dashboard(self):
        self.root.withdraw()
        from app.views.admin_dashboard import AdminDashboardWindow

        def on_close():
            self.root.deiconify()
            admin_window.root.destroy()

        admin_window = AdminDashboardWindow()
        admin_window.root.protocol("WM_DELETE_WINDOW", on_close)
        admin_window.run()

    def run(self):
        self.root.mainloop()
