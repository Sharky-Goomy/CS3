class Patient:
    _name = ""
    _bill_amount = 0.0
    def __init__(self, name, bill_amount):
        self._name = name
        self._bill_amount = bill_amount
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name
    def get_bill_amount(self):
        return self._bill_amount
    def set_bill_amount(self, bill_amount):
        self._bill_amount = bill_amount
    def calculate_bill(self):
        print(f"Original Bill: P{self._bill_amount}")
        print(f"Final Bill: P{self._bill_amount}")
    def display_patient_type(self):
        return "Regular Patient"

class SeniorPatient(Patient):
    def calculate_bill(self):
        print(f"Original Bill: P{self._bill_amount}")
        print(f"Final Bill: P{self._bill_amount * 0.8}")
    def display_patient_type(self):
        return "Senior Patient"

class PhillHealthPatient(Patient):
    def calculate_bill(self):
        print(f"Original Bill: P{self._bill_amount}")
        print(f"Final Bill: P{self._bill_amount * 0.85}")
    def display_patient_type(self):
        return "PhilHealth Patient"

patient = Patient("Juan Dela Cruz", 15000)
print(f"Patient Name: {patient.get_name()}")
print(f"Patient Type: {patient.display_patient_type()}")
patient.calculate_bill()

senior_patient = SeniorPatient("Maria Santos", 15000)
print(f"\nPatient Name: {senior_patient.get_name()}")
print(f"Patient Type: {senior_patient.display_patient_type()}")
senior_patient.calculate_bill()

philhealth_patient = PhillHealthPatient("Pedro Reyes", 15000)
print(f"\nPatient Name: {philhealth_patient.get_name()}")
print(f"Patient Type: {philhealth_patient.display_patient_type()}")
philhealth_patient.calculate_bill()