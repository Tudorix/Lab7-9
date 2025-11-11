class StudentRepo:
    def __init__(self):
        self.lista_studenti = []
        
    def rst(self):
        self.lista_studenti = []
        
    def exista_ID(self, ID):
        for e in self.lista_studenti:
            if ID == e.getID():
                return True
        return False
        
    def adauga_student(self , student):
        if self.exista_ID(student.getID()):
            print("There is nother student with that ID")
        else:
            self.lista_studenti.append(student)
            
    def sterge_student(self , ID):
        for i in range(len(self.lista_studenti)):
            if self.lista_studenti[i].getID() == int(ID):
                del self.lista_studenti[i]
                print("Student deleted successfully")
                return
                
        print("There is no student with that ID")
        
    def update_student(self , ID, newId, Nume):
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