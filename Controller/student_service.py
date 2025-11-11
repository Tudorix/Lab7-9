from Domain.student import Student

class ServiceStudent:
    def __init__(self, ValidatorStudent, RepoStudent):
        self.__validatorStudent = ValidatorStudent
        self.__repoStudent = RepoStudent
        
    def reset_list(self):
        self.__repoStudent.rst()
    
    def adauga_student(self , idStudent, Nume):
        student = Student(idStudent , Nume)
        try:
            self.__validatorStudent.validareStudent(student)
        except:
            print("Invalid Student")
            return
        
        self.__repoStudent.adauga_student(student)
        
    def sterge_student(self,idStudent):
        try:
            self.__validatorStudent.validareID(idStudent)
        except:
            print("ID is invalid")
            return
        
        self.__repoStudent.sterge_student(idStudent)
        
    def update_student(self,idStudent , newId , Nume):
        
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
        return self.__repoStudent.lista_studenti