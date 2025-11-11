class ValidatorDiscipline:
    
    def validareDiscilina(self, Disciplina):
        erori = []
        
        if Disciplina.getID() < 0:
            erori.append("IdError")

        if Disciplina.getNume() == "":
            erori.append("NumeError")
        
        if Disciplina.getProfesor() == "":
            erori.append("ProfesorError")
        
        if len(erori) > 0:
            raise erori
        
    def validareID(self, ID):
        try:
            ID = int(ID)
        except:
            raise Exception
            
        if ID < 0:
            raise Exception