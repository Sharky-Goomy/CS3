"""
Suliguin, Jose Santiago T.
9 - Balingkilat
Formative Assessment 3
November 12. 2026

"""


from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_reading(self):
        pass
    
class PHSensor(Sensor):
    def get_reading(self):
        return "[pH Sensor] Reading: 7.2 pH (Neutral)"

class TempSensor(Sensor):
    def get_reading(self):
        return "[Temperature Sensor] Reading: 24.5°C"

Sensor1 = PHSensor()
Sensor2 = TempSensor()

print("--- Lab Inventory System ---")
print(Sensor1.get_reading())
print(Sensor2.get_reading())
print()
print()
print("----------------------------")
