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
        
    def cautare_student(self, args):
        """ 
            Functie care cauta un student
            @param args - lista
        """
        if len(args) != 2:
            raise Exception
        
        case = 0
        
        if args[0] == "ID" : 
            case = 1
            try:
                self.__validatorStudent.validareID(args[1])
                if not self.__repoStudent.exista_ID(args[1]):
                    raise TypeError
            except:
                raise Exception
        elif args[0] == "Nume" :
            case = 2
            try:
                self.__validatorStudent.validareCuvant(args[1])
            except:
                raise Exception
        elif args[0] == "Varsta" : 
            case = 3
            try:
                self.__validatorStudent.validareVarsta(args[1])
            except:
                raise Exception
        else : raise Exception
        
        lista = self.get_studenti()
        lista_filtrata = []
        
        for e in self.get_studenti():
            if (case == 1 and e.getID() == int(args[1])) or (case == 2 and e.getNume() == args[1]) or (case == 3 and e.getVarsta() == int(args[1])):
                lista_filtrata.append(e)
        
        return lista_filtrata
        
    def reset_list(self):
        """
            Functie care reseteaza lista de studenti
        """
        self.__repoStudent.rst()
    
    def adauga_student(self , idStudent, Nume, Varsta):
        """
            Functie care adauga student in lista de studenti
            @param idStudent - int
            @param Nume - string
            @param Varsta - int
        """
        student = Student(idStudent , Nume.strip(), Varsta)
        try:
            self.__validatorStudent.validareStudent(student)
        except:
            raise ValueError
        
        self.__repoStudent.adauga_student(student)
        
    def sterge_student(self,idStudent):
        """
            Functie care sterge student din lista de studenti
            @param idStudent - int
        """
        try:
            self.__validatorStudent.validareID(idStudent)
        except:
            raise ValueError
        
        self.__repoStudent.sterge_student(idStudent)
        
    def update_student(self,idStudent , newId , Nume, Varsta):
        """
            Functie care modifica student din lista de studenti
            @param ID - string
            @param newId - int
            @param Nume - string
        """
        student = Student(newId , Nume, Varsta)
        try:
            self.__validatorStudent.validareStudent(student)
        except:
            raise ValueError
        
        try:
            self.__validatorStudent.validareID(idStudent)
        except:
            raise IndexError
        
        self.__repoStudent.update_student(idStudent, student)
        
    def get_studenti(self):
        """ 
            Functie care returneza lista curenta de studenti
        """
        return self.__repoStudent.getList()