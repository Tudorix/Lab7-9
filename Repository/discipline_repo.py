class DisciplineRepo:
    def __init__(self):
        """
            Constructorul clasei DisciplineRepo
        """
        self.lista_discipline = []
        
    def rst(self):
        """
            Functie care reseteaza lista de discipline
        """
        self.lista_discipline = []

    def exista_ID(self, ID):
        """
            Functie care verifica unicitatea ID-ului specificat
            @param ID - int
        """
        for e in self.lista_discipline:
            if ID == e.getID():
                return True
        return False

    def adauga_disciplina(self, disciplina):
        """
            Functie care adauga disciplina in lista de discipline
            @param disciplina - Disciplina
        """
        if self.exista_ID(disciplina.getID()):
            print("There is another Discipline with this ID")
        else:
            self.lista_discipline.append(disciplina)
        
    def sterge_disciplina(self, ID):
        """
            Functie care sterge disciplina din lista de discipline
            @param ID - string
        """
        for i in range(len(self.lista_discipline)):
            if self.lista_discipline[i].getID() == int(ID):
                del self.lista_discipline[i]
                print("Disciplina has been deleted successfully!")
                return
        print("There is no disciplina with that ID")
        
    def update_disciplina(self , ID , newID, Nume, Profesor):
        """
            Functie care modifica o disciplina din lista de discipline
            @param ID - string
            @param newID - int
            @param Nume - string
            @param Profesor - string
        """
        if self.exista_ID(newID) and int(ID) != newID:
            print("There is another Discipline with this ID")
        else:
            for i in range(len(self.lista_discipline)):
                if self.lista_discipline[i].getID() == int(ID):
                    self.lista_discipline[i].setID(newID)
                    self.lista_discipline[i].setNume(Nume)
                    self.lista_discipline[i].setProfesor(Profesor)
                    print("Disciplina has been updated successfully!")
                    return
                
            print("There is no disciplina with that ID")
        

