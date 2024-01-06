class Hospital:
    def __init__(self, admin_name):
        self.admin_name = admin_name
        self.patient_name = ""
        self.doctor_name = ""
        self.nurse_name = ""
        self.department_name = ""

    def get_patient_details(self):
        self.patient_name = input("Enter patient name: ")

    def get_doctor_details(self):
        self.doctor_name = input("Enter doctor name: ")

    def get_nurse_details(self):
        self.nurse_name = input("Enter nurse name: ")

    def get_department_details(self):
        self.department_name = input("Enter department name: ")

    def display_admin(self):
        print(f"Admin: {self.admin_name}")

    def display_doctor(self):
        print(f"Doctor Name: {self.doctor_name}")

    def display_nurse(self):
        print(f"Nurse Name: {self.nurse_name}")

    def display_department(self):
        print(f"Department: {self.department_name}")

class Department(Hospital):
    def __init__(self, admin_name, department_name):
        super().__init__(admin_name)
        self.department_name = department_name

    def display_all(self):
        self.display_admin()
        self.display_doctor()
        self.display_nurse()
        self.display_department()

class PatientWard(Hospital):
    def __init__(self, admin_name):
        super().__init__(admin_name)

    def get_patient_details(self):
        super().get_patient_details()

    def display_patient_details(self):
        self.display_admin()
        print(f"Patient Name: {self.patient_name}")

# Example Usage
admin_name = "Hospital Admin"
hospital_obj = Hospital(admin_name)

department_name = "Cardiology"
department_obj = Department(admin_name, department_name)

patient_ward_obj = PatientWard(admin_name)
patient_ward_obj.get_patient_details()

print("\nHospital Details:")
hospital_obj.get_doctor_details()
hospital_obj.get_nurse_details()
hospital_obj.get_department_details()

print("\nDepartment Details:")
department_obj.display_all()

print("\nPatient Details:")
patient_ward_obj.display_patient_details()
