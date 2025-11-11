class Disciplina:
    
    def __init__(self, ID , Nume, Profesor):
        self.ID = ID
        self.Nume = Nume
        self.Profesor = Profesor
        
    def getID(self):
        return self.ID
    
    def getNume(self):
        return self.Nume
    
    def getProfesor(self):
        return self.Profesor
    
    def setID(self, id):
        self.ID = id
    
    def setNume(self, nume):
        self.Nume = nume
    
    def setProfesor(self, profesor):
        self.Profesor = profesor
        
    def __str__(self):
        return f"({self.ID} , {self.Nume} , {self.Profesor})"
    
    def __repr__(self):
        return str(self)