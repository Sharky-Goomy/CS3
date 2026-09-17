class Mitochondria:
    def __init__(self):
        print("Mitochondria is created")
    def power_The_Cell(self):
        print("Mitochondria is providing power to the cell!")
    def __del__(self):
        print("The mitochondria is gone.")
        
class Nucleus:
    def __init__(self):
        print("Nucleus is created.")
    def __del__(self):
        print("The nucleus is gone.")
        
class Cell:
    def __init__(self):
        self.Mitochondria = Mitochondria()
        self.Nucleus = Nucleus()
        print("The cell is created!")
    def exists(self):
        self.Mitochondria.power_The_Cell()
        print("The cell has started existing!")

cellAtWork = Cell()
cellAtWork.exists()
