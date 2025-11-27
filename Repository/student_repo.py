from Domain.student import Student
class StudentRepo:
    def __init__(self , fileName):
        """
            Constructorul clasei StudentRepo
        """
        self.__lista_studenti = []
        self.__fileName = fileName
        self.load_from_file()
        
    def getList(self):
        """ 
            Functie care returneaza lista de studenti
        """
        return self.__lista_studenti

    def lenght(self):
        """ 
            Functie care returneaza lungimea lista de studenti
        """
        return len(self.__lista_studenti)
        
    def rst(self):
        """
            Functie care reseteaza lista de studenti
        """
        self.__lista_studenti = []
        
    def exista_ID(self, ID):
        """
            Functie care verifica daca ID exista in lista
            @param ID - int
        """
        for e in self.__lista_studenti:
            if ID == e.getID():
                return True
        return False
    
    def get_by_id(self, ID):
        """
            Functie care returneaza student daca ID exista in lista
            @param ID - int
            Raise - IndexError 
        """
        for e in self.__lista_studenti:
            if ID == e.getID():
                return e
        raise IndexError
        
    def adauga_student(self , student):
        """
            Functie care adauga student in lista de studenti
            @param student - Student
            Raise - IndexError 
        """
        if self.exista_ID(student.getID()):
            raise IndexError
        else:
            self.__lista_studenti.append(student)
            self.load_in_file()
            
    def sterge_student(self , ID):
        """
            Functie care sterge student din lista de studenti
            @param ID - string
            Raise - MemoryError 
        """
        for i in range(len(self.__lista_studenti)):
            if self.__lista_studenti[i].getID() == int(ID):
                del self.__lista_studenti[i]
                self.load_in_file()
                return
                
        raise MemoryError
        
    def update_student(self , ID, student):
        """
            Functie care modifica un student din lista de studenti
            @param ID - string
            @param student - Student
            Raise - MemoryError 
        """
        if self.exista_ID(student.getID()) and int(ID) != student.getID():
            print("There is nother student with that ID")
        else:
            for i in range(len(self.__lista_studenti)):
                if self.__lista_studenti[i].getID() == int(ID):
                    self.__lista_studenti[i] = student
                    self.load_in_file()
                    return
                    
            raise MemoryError
        
    def load_from_file(self):
        with open(self.__fileName,"r") as f:
            #reset the list
            self.rst()
            #preluare informatii pe linii
            lines = f.readlines()
            for l in lines:
                parts = l.split(",")
                #Preluare informatii
                ID = int(parts[0])
                Nume = parts[1]
                Varsta = int(parts[2])
                student = Student(ID , Nume , Varsta)
                self.adauga_student(student)
        
    def load_in_file(self):
        with open(self.__fileName , "w") as f:
            for i in self.__lista_studenti:
                f.writelines(f"{i.getID()},{i.getNume()},{i.getVarsta()}\n")