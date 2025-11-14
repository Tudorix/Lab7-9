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
            com = input("Enter a command:\n>>>")
            args = com.strip().split()
            
            if args[0] == "exit":
                running = False
            elif args[0] == "help":
                print("Commands list:\n" + 
                    "exit\n" + 
                    "add student/disciplina\n" + 
                    "update student/disciplina\n" + 
                    "delete student/disciplina\n" + 
                    "print student/disciplina")
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
                    
            elif args[0] == "add":
                if len(args) <= 1:
                    print("You forgot to specify the type(student/disciplina)")
                elif args[1] == "student":
                    (ID , nume, varsta) = self.citeste_student()
                    try:
                        self.serviceStudenti.adauga_student(ID , nume, varsta)
                    except ValueError:
                        print("Invalid Student")
                    except IndexError:
                        print("There is another Student with that ID")
                elif args[1] == "disciplina":
                    (ID , nume, profesor) = self.citeste_disciplina()
                    self.serviceDiscipline.adauga_disciplina(ID , nume, profesor)
                    
            elif args[0] == "del":
                if len(args) <= 1:
                    print("You forgot to specify the type(student/disciplina)")
                elif args[1] == "student":
                    
                    if len(args) <= 2:
                        print("You forgot to specify the student ID")
                    else:
                        self.serviceStudenti.sterge_student(args[2])
                elif args[1] == "disciplina":
                    
                    if len(args) <= 2:
                        print("You forgot to specify the disciplina ID")
                    else:
                        self.serviceDiscipline.sterge_disciplina(args[2])
                        
            elif args[0] == "update":
                if len(args) <= 1:
                    print("You forgot to specify the type(student/disciplina)")
                elif args[1] == "student":
                    
                    if len(args) <= 2:
                        print("You forgot to specify the student ID")
                    else:
                        (ID , nume, varsta) = self.citeste_student()
                        self.serviceStudenti.update_student(args[2],ID, nume, varsta)
                        
                elif args[1] == "disciplina":
                    
                    if len(args) <= 2:
                        print("You forgot to specify the disciplina ID")
                    else:
                        (ID , nume, profesor) = self.citeste_disciplina()
                        self.serviceDiscipline.update_disciplina(args[2],ID, nume, profesor)
                        
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
                        
                elif args[1] == "disciplina":
                    
                    if len(args) <= 2:
                        print("You forgot to specify the disciplina ID")
                    else:
                        (ID , nume, profesor) = self.citeste_disciplina()
                        self.serviceDiscipline.update_disciplina(args[2],ID, nume, profesor)
                        
            else:
                print("Invalid command")