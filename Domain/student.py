class Student:
    def __init__(self, ID, Nume):
        self.ID = ID
        self.Nume = Nume
        
    def __str__(self):
        return f"({self.ID} , {self.Nume})"
    
    def getNume(self):
        return self.Nume
    
    def getID(self):
        return self.ID
    
    def setNume(self, name):
        self.Nume = name
    
    def setID(self, id):
        self.ID = id