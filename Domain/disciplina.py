class Disciplina:
    
    def __init__(self, ID , Nume, Profesor):
        """
            Constructorul clasei Student
            @param ID - int
            @param Nume - string
            @param Profesor - string
        """
        self.ID = ID
        self.Nume = Nume
        self.Profesor = Profesor
        
    def getID(self):
        """
            Getter pentru ID Disciplina
        """
        return self.ID
    
    def getNume(self):
        """
            Getter pentru Nume Disciplina
        """
        return self.Nume
    
    def getProfesor(self):
        """
            Getter pentru Profesor Disciplina
        """
        return self.Profesor
    
    def setID(self, id):
        """
            Setter pentru ID Disciplina
            @param id - int
        """
        self.ID = id
    
    def setNume(self, nume):
        """
            Setter pentru Nume Disciplina
            @param Nume - string
        """
        self.Nume = nume
    
    def setProfesor(self, profesor):
        """
            Setter pentru Profesor Disciplina
            @param Profesor - string
        """
        self.Profesor = profesor
        
    def __str__(self):
        """
            Functie care schimba obiectul Disciplina sub forma unui string
        """
        return f"({self.ID} , {self.Nume} , {self.Profesor})"
    
    def __repr__(self):
        """
            Functie care schimba reprezentarea obiectului Disciplina sub forma unui string
        """
        return str(self)