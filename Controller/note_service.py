from Domain.nota import Nota
class ServiceNote:
    
    def __init__(self, ValidatorNota , RepoNota):
        self.__validatorNota = ValidatorNota
        self.__repoNota = RepoNota
        
    def get_note(self):
        return self.__repoNota.get_note()
        
    def adauga_nota(self , ID , Valoare, Student , Disciplina):
        nota = Nota(Student , Disciplina , Valoare , ID)
        try:
            self.__validatorNota.validareNota(nota)
        except:
            raise Exception
        
        self.__repoNota.adauga_nota(nota)
        
    def sterge_nota(self, ID):
        
        try:
            self.__validatorNota.validareID(ID)
        except:
            raise ValueError
        
        self.__repoNota.sterge_nota(ID)