class Student:
    def __init__(self, ID, Nume):
        """
            Constructorul clasei Student
            @param ID - int
            @param Nume - string
        """
        self.ID = ID
        self.Nume = Nume
        
    def __str__(self):
        """
            Functie care returneaza obiectul Student sub forma unui string
        """
        return f"({self.ID} , {self.Nume})"
    
    def __repr__(self):
        """
            Functie care returneaza reprezentarea obiectului Student sub forma unui string
        """
        return str(self)
    
    def getNume(self):
        """
            Getter pentru Nume Studnet
        """
        return self.Nume
    
    def getID(self):
        """
            Getter pentru ID Studnet
        """
        return self.ID
    
    def setNume(self, name):
        """
            Setter pentru Nume Studnet
            @param name - string
        """
        self.Nume = name
    
    def setID(self, id):
        """
            Setter pentru ID Studnet
            @param id - int
        """
        self.ID = id