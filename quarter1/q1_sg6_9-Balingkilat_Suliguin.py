#15 - Suliguin, Jose Santiago T.
9 - Balingkilat
SG2 - Activity 3
September 10, 2026 

class Lab:
    def __init__(self, room_number):
        self.room_number = room_number
class Technician:
    def __init__(self, name):
        self.name = name
        self.assigned_lab = None
    def assign_lab(self, Lab):
        self.assigned_lab = Lab

chem_lab = Lab("302")
mr_cruz = Technician('Mr. Cruz')
mr_cruz.assign_lab(chem_lab)
print(mr_cruz.assigned_lab.room_number)
