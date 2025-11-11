class TestStudent:
    
    def __init__(self, serviceStudenti):
        self.serviceStudenti = serviceStudenti
    
    def test_adauga_student(self):
        self.serviceStudenti.reset_list()
        self.serviceStudenti.adauga_student(48 , "Tudor")
        assert str(self.serviceStudenti.get_studenti()) == "[(48 , Tudor)]"
        self.serviceStudenti.adauga_student(56 , "Andrei")
        assert str(self.serviceStudenti.get_studenti()) == "[(48 , Tudor), (56 , Andrei)]"
        
    def test_update_student(self):
        self.serviceStudenti.reset_list()
        self.serviceStudenti.adauga_student(48 , "Tudor")
        self.serviceStudenti.adauga_student(56 , "Andrei")
        self.serviceStudenti.update_student("48", 36, "Stefan")
        assert str(self.serviceStudenti.get_studenti()) == "[(36 , Stefan), (56 , Andrei)]"
        
    def test_stergere_student(self):
        self.serviceStudenti.reset_list()
        self.serviceStudenti.adauga_student(48 , "Tudor")
        self.serviceStudenti.adauga_student(56 , "Andrei")
        self.serviceStudenti.sterge_student(48)
        assert str(self.serviceStudenti.get_studenti()) == "[(56 , Andrei)]"

    def test_all(self):
        self.test_adauga_student()
        self.test_update_student()
        self.test_stergere_student()