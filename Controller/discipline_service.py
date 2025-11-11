from Domain.disciplina import Disciplina

class ServiceDiscipline:
    def __init__(self, ValidatorDisciplina, RepoDisciplina):
        self.__validatorDisciplina = ValidatorDisciplina
        self.__repoDisciplina = RepoDisciplina
        
    def reset_list(self):
        self.__repoDisciplina.rst()
        
    def get_discipline(self):
        return self.__repoDisciplina.lista_discipline

    def adauga_disciplina(self , ID, Nume, Profesor):
        disciplina = Disciplina(ID , Nume, Profesor)
        try:
            self.__validatorDisciplina.validareDiscilina(disciplina)
        except:
            print("Invalid Discipline")
            return
        
        self.__repoDisciplina.adauga_disciplina(disciplina)
        
    def sterge_disciplina(self, ID):
        try:
            self.__validatorDisciplina.validareID(ID)
        except:
            print("ID is Invalid")
            return

        self.__repoDisciplina.sterge_disciplina(ID)
        
    def update_disciplina(self,idDisciplina , newId , Nume, Profesor):
        
        try:
            self.__validatorDisciplina.validareID(newId)
        except:
            print("New ID is invalid")
            return
        
        try:
            self.__validatorDisciplina.validareID(idDisciplina)
        except:
            print("Existing ID is invalid")
            return
        
        self.__repoDisciplina.update_disciplina(idDisciplina, newId , Nume, Profesor)