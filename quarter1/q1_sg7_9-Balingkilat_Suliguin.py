#15 - Suliguin, Jose Santiago T.
9 - Balingkilat
SG2 - Activity 3
September 10, 2026 

class Glassware:
    def __init__(self, glassware):
        self.glassware = glassware

class Beaker(Glassware):
    def __init__(self, glassware, beaker):
        super().__init__(glassware)
        self.beaker = beaker

class Tray:
    def __init__(self, tray):
        self.tray = tray
        self.container = []
        for i in range(1,6):
          Glass_Beaker = Beaker("Glassware", "Glass_Beaker")
          self.container.append(Glass_Beaker)
        
Gray_Tray = Tray("Gray Tray",)

for Glass_Beaker in Gray_Tray.container:
    print(Glass_Beaker.beaker)
    print()
