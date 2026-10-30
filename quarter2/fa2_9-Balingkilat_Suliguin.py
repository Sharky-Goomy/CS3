"""
Suliguin, Jose Santiago T.
9 - Balingkilat
October 22, 2026
CS3 - Q2 - FA2
"""

class Patient:
    __name = ""
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount
    def get_bill_amount(self):
        return self.__bill_amount
    def calculate_bill(self):
        final_bill = self.__bill_amount
        return final_bill
    def display_info(self):
        Final_Bill = self.calculate_bill()
        print(f"Patient Name: {self.__name}")
        print(f"Original Bill: ₱{(self.__bill_amount):,.2f}")
        print(f"Final_Bill: ₱{float(Final_Bill):,.2f}")

class Senior_Patient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)
    def calculate_bill(self):
        bill_amount = self.get_bill_amount()
        discount_factor = 0.20
        discount_price = discount_factor * bill_amount
        final_bill = bill_amount - discount_price
        return final_bill
    def display_info(self):
        super().display_info()

class PhilHealth_Patient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)
    def calculate_bill(self):
        bill_amount = self.get_bill_amount()
        discount_factor = 0.15
        discount_price = discount_factor * bill_amount
        final_bill = bill_amount - discount_price
        return final_bill
    def display_info(self):
        super().display_info()

print("Hospital Billing System")
print("------------------------")
patient_name = Patient("Juan Dela Cruz", 15000)
patient_name.display_info()
print()
Senior_Name = Senior_Patient("Maria Santos", 15000)
Senior_Name.display_info()
print()
PhilHealth_Name = PhilHealth_Patient("Pedro Reyes", 15000)
PhilHealth_Name.display_info()


