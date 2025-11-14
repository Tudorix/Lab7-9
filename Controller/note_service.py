from Domain.nota import Nota
class ServiceNote:
    
    def __init__(self, RepoNota, ValidatorNota):
        self.__validatorNota = ValidatorNota
        self.__repoNota = RepoNota
        
    def adauga_nota(self , ID , Valoare, Student , Disciplina):
        nota = Nota(Student , Disciplina , Valoare , ID)
        try:
            self.__validatorNota.validareNota(nota)
        except:
            raise Exception
        
        self.__repoNota.adauga_nota(nota)