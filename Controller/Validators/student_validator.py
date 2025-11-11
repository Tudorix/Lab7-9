class ValidatorStudent:
    
    def validareStudent(self, Student):
        erori = []
        
        if Student.getID() < 0:
            erori.append("IdError")

        if Student.getNume() == "":
            erori.append("NumeError")

        if len(erori) > 0:
            raise erori
        
    def validareID(self, ID):
        try:
            ID = int(ID)
        except:
            raise Exception
            
        if ID < 0:
            raise Exception