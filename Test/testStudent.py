class TestStudent:
    
    def __init__(self, serviceStudenti):
        """ 
            Functie de initiere pentru modulul de teste alocat Student
        """
        self.serviceStudenti = serviceStudenti
    
    def test_adauga_student(self):
        """ 
            Functie de test pentru adauga_student
        """
        self.serviceStudenti.reset_list()
        self.serviceStudenti.adauga_student(48 , "Tudor", 19)
        assert self.serviceStudenti.get_studenti()[0].getNume() == "Tudor"
        assert self.serviceStudenti.get_studenti()[0].getID() == 48
        assert self.serviceStudenti.get_studenti()[0].getVarsta() == 19
        self.serviceStudenti.adauga_student(56 , "Andrei", 23)
        assert self.serviceStudenti.get_studenti()[1].getNume() == "Andrei"
        assert self.serviceStudenti.get_studenti()[1].getID() == 56
        assert self.serviceStudenti.get_studenti()[1].getVarsta() == 23
        
    def test_update_student(self):
        """ 
            Functie de test pentru update_student
        """
        self.serviceStudenti.reset_list()
        self.serviceStudenti.adauga_student(48 , "Tudor", 19)
        self.serviceStudenti.adauga_student(56 , "Andrei", 23)
        self.serviceStudenti.update_student("56", 36, "Stefan", 18)
        assert self.serviceStudenti.get_studenti()[1].getNume() == "Stefan"
        assert self.serviceStudenti.get_studenti()[1].getID() == 36
        assert self.serviceStudenti.get_studenti()[1].getVarsta() == 18
        
    def test_stergere_student(self):
        """ 
            Functie de test pentru stergere_student
        """
        self.serviceStudenti.reset_list()
        self.serviceStudenti.adauga_student(48 , "Tudor", 19)
        self.serviceStudenti.adauga_student(56 , "Andrei", 23)
        self.serviceStudenti.sterge_student(48)
        assert self.serviceStudenti.get_studenti()[0].getNume() == "Andrei"
        assert self.serviceStudenti.get_studenti()[0].getID() == 56
        assert self.serviceStudenti.get_studenti()[0].getVarsta() == 23

    def test_all(self):
        """ 
            Functie de test pentru toate functiile de test
        """
        self.test_adauga_student()
        self.test_update_student()
        self.test_stergere_student()