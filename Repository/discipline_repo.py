class DisciplineRepo:
    def __init__(self):
        self.lista_discipline = []

    def exista_ID(self, ID):
        for e in self.lista_discipline:
            if ID == e.getID():
                return True
        return False
    
    def adauga_disciplina(self, disciplina):
        if self.exista_ID(disciplina.getID()):
            print("There is another Discipline with this ID")
        else:
            self.lista_discipline.append(disciplina)

    def sterge_disciplina(self, ID):
        for i in range(len(self.lista_discipline)):
            if ID == self.lista_discipline[i].getID == ID:
                del self.lista_discipline[i]
                print("Disciplina has been deleted successfully!")
                return

