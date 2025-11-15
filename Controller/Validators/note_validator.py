class ValidatorNota:
    
    def validareNota(self, Nota):
        erori = []
        
        if Nota.getValoare() < 0 or Nota.getValoare() > 10:
            erori.append("ValoareError")
        if Nota.getID() < 0:
            erori.append("IdError")
        
        if len(erori) > 0:
            raise erori
        