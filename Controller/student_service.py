from Domain.student import Student

class ServiceStudent:
    def __init__(self, ValidatorStudent, RepoStudent):
        """
            Constructorul clasei ServiceStudent
            @param ValidatorStudent - ValidatorStudent
            @param RepoStudent - StudentRepo
        """
        self.__validatorStudent = ValidatorStudent
        self.__repoStudent = RepoStudent
        
    def reset_list(self):
        """
            Functie care reseteaza lista de studenti
        """
        self.__repoStudent.rst()
    
    def adauga_student(self , idStudent, Nume):
        """
            Functie care adauga student in lista de studenti
            @param idStudent - int
            @param Nume - string
        """
        student = Student(idStudent , Nume)
        try:
            self.__validatorStudent.validareStudent(student)
        except:
            print("Invalid Student")
            return
        
        self.__repoStudent.adauga_student(student)
        
    def sterge_student(self,idStudent):
        """
            Functie care sterge student din lista de studenti
            @param idStudent - int
        """
        try:
            self.__validatorStudent.validareID(idStudent)
        except:
            print("ID is invalid")
            return
        
        self.__repoStudent.sterge_student(idStudent)
        
    def update_student(self,idStudent , newId , Nume):
        """
            Functie care modifica student din lista de studenti
            @param ID - string
            @param newId - int
            @param Nume - string
        """
        try:
            self.__validatorStudent.validareID(newId)
        except:
            print("New ID is invalid")
            return
        
        try:
            self.__validatorStudent.validareID(idStudent)
        except:
            print("Existing ID is invalid")
            return
        
        self.__repoStudent.update_student(idStudent, newId , Nume)
        
    def get_studenti(self):
        """ 
            Functie care returneza lista curenta de studenti
        """
        return self.__repoStudent.lista_studenti