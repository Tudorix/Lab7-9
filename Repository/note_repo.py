class NoteRepo:
    def __init__(self):
        self.__lista_note = []
        
    def get_note(self):
        return self.__lista_note
        
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
            
    def sterge_nota(self , ID):
        """
            Functie care sterge nota din lista de note
            @param ID - string
        """
        for i in range(len(self.__lista_note)):
            if self.__lista_note[i].getID() == int(ID):
                del self.__lista_note[i]
                return
                
        raise MemoryError