class Hero:
    def __init__(self, name, HP):
        self.name = name
        self.HP = HP
    def Take_damage(self, damage):
        self.HP -= damage
        
Arthur = Hero("Arthur", 700)
Morgana = Hero("Morgana", 550)

Arthur.Take_damage(10) 
print("After a rough battle against monsters, Arthur has lost 10 HP, leaving only behind:", Arthur.HP, "HP left. Luckily, Morgana has been left unscathed with no injuries and damage, with", Morgana.HP, "HP left")

        
