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
        self.serviceStudenti.adauga_student(48 , "Tudor")
        assert str(self.serviceStudenti.get_studenti()) == "[(48 , Tudor)]"
        self.serviceStudenti.adauga_student(56 , "Andrei")
        assert str(self.serviceStudenti.get_studenti()) == "[(48 , Tudor), (56 , Andrei)]"
        
    def test_update_student(self):
        """ 
            Functie de test pentru update_student
        """
        self.serviceStudenti.reset_list()
        self.serviceStudenti.adauga_student(48 , "Tudor")
        self.serviceStudenti.adauga_student(56 , "Andrei")
        self.serviceStudenti.update_student("48", 36, "Stefan")
        assert str(self.serviceStudenti.get_studenti()) == "[(36 , Stefan), (56 , Andrei)]"
        
    def test_stergere_student(self):
        """ 
            Functie de test pentru stergere_student
        """
        self.serviceStudenti.reset_list()
        self.serviceStudenti.adauga_student(48 , "Tudor")
        self.serviceStudenti.adauga_student(56 , "Andrei")
        self.serviceStudenti.sterge_student(48)
        assert str(self.serviceStudenti.get_studenti()) == "[(56 , Andrei)]"

    def test_all(self):
        """ 
            Functie de test pentru toate functiile de test
        """
        self.test_adauga_student()
        self.test_update_student()
        self.test_stergere_student()