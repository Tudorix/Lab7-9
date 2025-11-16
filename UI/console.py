class Console:
    
    def __init__(self, serviceStudenti, serviceDiscipline, serviceNote):
        """
            Constructorul clasei Console
            @param serviceStudenti - ServiceStudent
            @param serviceDiscipline - ServiceDiscipline
            @param serviceNote - ServiceNote
        """
        self.serviceStudenti = serviceStudenti
        self.serviceDiscipline = serviceDiscipline
        self.serviceNote = serviceNote
    
    def citeste_student(self):
        """
            Functie care citeste datele pentru obiectul student
        """
        id = None
        nume = ""
        varsta = None
        
        while True:
            try:
                id = int(input("Enter the ID\n>>>")) 
                break
            except ValueError:
                print("ID invalid")
                
        while True:
            try:
                varsta = int(input("Enter the Age\n>>>")) 
                break
            except ValueError:
                print("Age invalid")
        
        while nume == "":
            nume = input("Enter the Name\n>>>")
        
        return (id , nume, varsta)
    
    def citeste_nota(self):
        """
            Functie care citeste datele pentru obiectul student
        """
        idNota = None
        valoare = -1
        idStudent = None
        idDisciplina = None
        
        while True:
            try:
                idNota = int(input("Enter the ID of the Nota\n>>>")) 
                break
            except ValueError:
                print("Nota ID invalid")
                
        while True:
            try:
                valoare = int(input("Enter the value of Nota\n>>>")) 
                if valoare > 0 and valoare <= 10:
                    break
            except ValueError:
                print("Nota value invalid")
                
        while True:
            try:
                idStudent = int(input("Enter the ID of the Student\n>>>")) 
                break
            except ValueError:
                print("Student ID invalid")
                
        while True:
            try:
                idDisciplina = int(input("Enter the ID of the Disciplina\n>>>")) 
                break
            except ValueError:
                print("Disciplina ID invalid")
                
        return (idNota , valoare, idStudent , idDisciplina)
    
    def citeste_disciplina(self):
        """
            Functie care citeste datele pentru obiectul disciplina
        """
        id = None
        nume = ""
        profesor = ""
        
        while True:
            try:
                id = int(input("Enter the ID\n>>>")) 
                break
            except ValueError:
                print("ID invalid")
        
        while nume == "":
            nume = input("Enter the Name\n>>>")
            
        while profesor == "":
            profesor = input("Enter the Profssor\n>>>")
        
        return (id , nume , profesor)
    
    def run(self):
        print("Type 'help' to see the commands")
        running = True
        
        while running:
            try:
                com = input("Enter a command:\n>>>")
                args = com.strip().split()
                
                if args[0] == "exit":
                    running = False
                elif args[0] == "help":
                    print("Commands list:\n" + 
                        "exit\n" + 
                        "add student/disciplina/nota\n" + 
                        "update student/disciplina\n" + 
                        "del student/disciplina/nota\n" + 
                        "print student/disciplina/nota")
                elif args[0] == "print":
                    if len(args) <= 1:
                        print("You forgot to specify the type(student/disciplina)")
                    elif args[1] == "student":
                        print("Studenti:")
                        lista = self.serviceStudenti.get_studenti()
                        for e in lista:
                            print(e)
                    elif args[1] == "disciplina":
                        print("Discipline:")
                        lista = self.serviceDiscipline.get_discipline()
                        for e in lista:
                            print(e)
                    elif args[1] == "nota":
                        print("Note:")
                        lista = self.serviceNote.get_note()
                        for e in lista:
                            print(e)
                        
                elif args[0] == "add":
                    if len(args) <= 1:
                        print("You forgot to specify the type(student/disciplina)")
                    elif args[1] == "student":
                        (ID , nume, varsta) = self.citeste_student()
                        try:
                            self.serviceStudenti.adauga_student(ID , nume, varsta)
                            print("Student added successfully")
                        except ValueError:
                            print("Invalid Student")
                        except IndexError:
                            print("There is another Student with that ID")
                    elif args[1] == "disciplina":
                        (ID , nume, profesor) = self.citeste_disciplina()
                        try:
                            self.serviceDiscipline.adauga_disciplina(ID , nume, profesor)
                            print("Disciplina added successfully")
                        except ValueError:
                            print("Invalid Disciplina")
                        except IndexError:
                            print("There is another Discipline with this ID")
                    elif args[1] == "nota":
                        (idNota , valoare, idStudent , idDisciplina) = self.citeste_nota()
                        try:
                            argumente = ["ID" , idStudent]
                            student = self.serviceStudenti.cautare_student(argumente)[0]
                            argumente = ["ID" , idDisciplina]
                            disciplina = self.serviceDiscipline.cautare_disciplina(argumente)[0]
                            self.serviceNote.adauga_nota(idNota , valoare, student , disciplina)
                            print("Nota added successfully")
                        except:
                            print("Invalid Nota")
                        
                elif args[0] == "del":
                    if len(args) <= 1:
                        print("You forgot to specify the type(student/disciplina)")
                    elif args[1] == "student":
                        
                        if len(args) <= 2:
                            print("You forgot to specify the student ID")
                        else:
                            try:
                                self.serviceStudenti.sterge_student(args[2])
                                print("Student deleted successfully")
                            except MemoryError:
                                print("There is no Student with that ID")
                            except ValueError:
                                print("ID is invalid")
                                
                    elif args[1] == "disciplina":
                        
                        if len(args) <= 2:
                            print("You forgot to specify the disciplina ID")
                        else:
                            try:
                                self.serviceDiscipline.sterge_disciplina(args[2])
                                print("Disciplina deleted successfully")
                            except MemoryError:
                                print("There is no Disciplina with that ID")
                            except ValueError:
                                print("ID is invalid")
                    elif args[1] == "nota":
                        
                        if len(args) <= 2:
                            print("You forgot to specify the nota ID")
                        else:
                            try:
                                self.serviceNote.sterge_nota(args[2])
                                print("Nota deleted successfully")
                            except MemoryError:
                                print("There is no Nota with that ID")
                            except ValueError:
                                print("ID is invalid")
                            
                elif args[0] == "update":
                    if len(args) <= 1:
                        print("You forgot to specify the type(student/disciplina)")
                    elif args[1] == "student":
                        
                        if len(args) <= 2:
                            print("You forgot to specify the student ID")
                        else:
                            (ID , nume, varsta) = self.citeste_student()
                            try:
                                self.serviceStudenti.update_student(args[2],ID, nume, varsta)
                                print("Student updated successfully")
                            except MemoryError:
                                print("There is no Student with that ID")
                            except ValueError:
                                print("Invalid Student")
                            except IndexError:
                                print("Existing ID is invalid")
                            
                    elif args[1] == "disciplina":
                        
                        if len(args) <= 2:
                            print("You forgot to specify the disciplina ID")
                        else:
                            (ID , nume, profesor) = self.citeste_disciplina()
                            try:
                                self.serviceDiscipline.update_disciplina(args[2],ID, nume, profesor)
                                print("Disciplina updated successfully")
                            except MemoryError:
                                print("There is no Disciplina with that ID")
                            except ValueError:
                                print("Invalid Disciplina")
                            except IndexError:
                                print("Existing ID is invalid")
                            
                elif args[0] == "cauta":
                    if len(args) <= 1:
                        print("You forgot to specify the type(student/disciplina)")
                    elif args[1] == "student":
                        
                        if len(args) <= 2:
                            print("You forgot to specify the criteria")
                        else:
                            try:
                                argumente = args[2:]
                                lista = self.serviceStudenti.cautare_student(argumente)
                                for e in lista:
                                    print(e)
                            except:
                                print("Invalid arguments")
                    elif args[1] == "disciplina":
                        
                        if len(args) <= 2:
                            print("You forgot to specify the criteria")
                        else:
                            try:
                                argumente = args[2:]
                                lista = self.serviceDiscipline.cautare_disciplina(argumente)
                                for e in lista:
                                    print(e)
                            except:
                                print("Invalid arguments")
                            
                else:
                    print("Invalid command")
            except:
                print ("Invalid command")