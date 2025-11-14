class NoteRepo:
    def __init__(self):
        self.__lista_note = []
        
    def exista_ID(self, ID):
        for e in self.__lista_note:
            if e.getID() == ID:
                return True
        return False
        
    def adauga_nota(self, Nota):
        if self.exista_ID(Nota.getID()):
            print("There is another Nota with that ID")
        else:
            self.__lista_note.append(Nota)