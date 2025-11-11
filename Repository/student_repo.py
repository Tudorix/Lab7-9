class StudentRepo:
    def __init__(self):
        """
            Constructorul clasei StudentRepo
        """
        self.lista_studenti = []
        
    def rst(self):
        """
            Functie care reseteaza lista de studenti
        """
        self.lista_studenti = []
        
    def exista_ID(self, ID):
        """
            Functie care verifica unicitatea ID-ului specificat
            @param ID - int
        """
        for e in self.lista_studenti:
            if ID == e.getID():
                return True
        return False
        
    def adauga_student(self , student):
        """
            Functie care adauga student in lista de studenti
            @param student - Student
        """
        if self.exista_ID(student.getID()):
            print("There is nother student with that ID")
        else:
            self.lista_studenti.append(student)
            
    def sterge_student(self , ID):
        """
            Functie care sterge student din lista de studenti
            @param ID - string
        """
        for i in range(len(self.lista_studenti)):
            if self.lista_studenti[i].getID() == int(ID):
                del self.lista_studenti[i]
                print("Student deleted successfully")
                return
                
        print("There is no student with that ID")
        
    def update_student(self , ID, newId, Nume):
        """
            Functie care modifica un student din lista de studenti
            @param ID - string
            @param newId - int
            @param Nume - string
        """
        if self.exista_ID(newId) and int(ID) != newId:
            print("There is nother student with that ID")
        else:
            for i in range(len(self.lista_studenti)):
                if self.lista_studenti[i].getID() == int(ID):
                    self.lista_studenti[i].setID(newId)
                    self.lista_studenti[i].setNume(Nume)
                    print("Student updated successfully")
                    return
                    
            print("There is no student with that ID")