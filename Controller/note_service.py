from Domain.nota import Nota
import random
class ServiceNote:
    
    def __init__(self, ValidatorNota , RepoNota , RepoStudent , RepoDiciplina):
        """
            Constructorul clasei ServiceDiscipline
            @param ValidatorNota - ValidatorNota
            @param RepoNota - NotaRepo
        """
        self.__validatorNota = ValidatorNota
        self.__repoNota = RepoNota
        self.__repoStud = RepoStudent
        self.__repoDisc = RepoDiciplina
        
    def reset_list(self):
        """
            Functie care reseteaza lista de note
        """
        self.__repoNota.rst()
        
    def get_note(self):
        """ 
            Functie care returneza lista curenta de note
        """
        return self.__repoNota.get_note()
        
    def adauga_nota(self , ID , Valoare, idStudent , idDisciplina):
        """
            Functie care adauga nota in lista de note
            @param ID - int
            @param Valoare - int
            @param Student - Student
            @param Disciplina - Disciplina
        """
        
        Student = self.__repoStud.get_by_id(idStudent)
        Disciplina = self.__repoDisc.get_by_id(idDisciplina)
        
        nota = Nota(Student , Disciplina , Valoare , ID)
        try:
            self.__validatorNota.validareNota(nota)
        except:
            raise Exception
        
        self.__repoNota.adauga_nota(nota)
        
    def gen_studenti(self , nr):
        while nr >= 0:
            varsta = random.randint(18 , 30)
            id = random.randint(0 , 1000)
            
        
    def sterge_nota(self, ID):
        """
            Functie care sterge nota din lista de note
            @param ID - int
        """
        try:
            self.__validatorNota.validareID(ID)
        except:
            raise ValueError
        
        self.__repoNota.sterge_nota(ID)