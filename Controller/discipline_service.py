from Domain.disciplina import Disciplina

class ServiceDiscipline:
    def __init__(self, ValidatorDisciplina, RepoDisciplina):
        """
            Constructorul clasei ServiceDiscipline
            @param ValidatorDisciplina - ValidatorDisciplina
            @param RepoDisciplina - DisciplinaRepo
        """
        self.__validatorDisciplina = ValidatorDisciplina
        self.__repoDisciplina = RepoDisciplina
        
    def reset_list(self):
        """
            Functie care reseteaza lista de discipline
        """
        self.__repoDisciplina.rst()
        
    def get_discipline(self):
        """ 
            Functie care returneza lista curenta de discipline
        """
        return self.__repoDisciplina.getList()

    def adauga_disciplina(self , ID, Nume, Profesor):
        """
            Functie care adauga disciplina in lista de discipline
            @param ID - int
            @param Nume - string
            @param Profesor - string
        """
        disciplina = Disciplina(ID , Nume, Profesor)
        try:
            self.__validatorDisciplina.validareDiscilina(disciplina)
        except:
            print("Invalid Discipline")
            return
        
        self.__repoDisciplina.adauga_disciplina(disciplina)
        
    def sterge_disciplina(self, ID):
        """
            Functie care sterge disciplina din lista de discipline
            @param ID - int
        """
        try:
            self.__validatorDisciplina.validareID(ID)
        except:
            print("ID is Invalid")
            return

        self.__repoDisciplina.sterge_disciplina(ID)
        
    def update_disciplina(self,idDisciplina , newId , Nume, Profesor):
        """
            Functie care modifica disciplina din lista de discipline
            @param idDisciplina - string
            @param newId - int
            @param Nume - string
            @param Profesor - string
        """
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