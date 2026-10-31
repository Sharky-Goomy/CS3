"""
#15 - Suliguin, Jose Santiago T.
#18 - Bernardo, Aeden Ysabel M.
#22 - Dogillo, Charlize Sky A.
9-Balingkilat
October 30, 2026
CS3 - SG11 - Activity 4

"""
class HealthPotion():
    def use(self):
        print("You regain 50 HP!")

class ManaPotion():
    def use(self):
        print("You restore 30 MP!")

class SpeedBoost():
    def use(self):
        print("Your speed increases for 10 seconds!")

def apply_item(item):
    item.use()

items = [HealthPotion(), ManaPotion(), SpeedBoost()]
for item in items:
    apply_item(item)
