class TestDiscipline:
    
    def __init__(self, serviceDiscipline):
        """ 
            Functie de initiere pentru modulul de teste alocat Disciplina
        """
        self.serviceDiscipline = serviceDiscipline
        
    def test_adauga_disciplina(self):
        """ 
            Functie de test pentru adauga_disciplina
        """
        self.serviceDiscipline.reset_list()
        self.serviceDiscipline.adauga_disciplina(12 , "Mate", "Stefan")
        assert self.serviceDiscipline.get_discipline()[0].getID() == 12
        assert self.serviceDiscipline.get_discipline()[0].getNume() == "Mate"
        assert self.serviceDiscipline.get_discipline()[0].getProfesor() == "Stefan"
        self.serviceDiscipline.adauga_disciplina(24 , "Info", "Daniela")
        assert self.serviceDiscipline.get_discipline()[1].getID() == 24
        assert self.serviceDiscipline.get_discipline()[1].getNume() == "Info"
        assert self.serviceDiscipline.get_discipline()[1].getProfesor() == "Daniela"
        
    def test_update_disciplina(self):
        """ 
            Functie de test pentru update_disciplina
        """
        self.serviceDiscipline.reset_list()
        self.serviceDiscipline.adauga_disciplina(12 , "Mate", "Stefan")
        self.serviceDiscipline.adauga_disciplina(24 , "Info", "Daniela")
        self.serviceDiscipline.update_disciplina(24,36, "FP", "Gabi")
        assert self.serviceDiscipline.get_discipline()[1].getID() == 36
        assert self.serviceDiscipline.get_discipline()[1].getNume() == "FP"
        assert self.serviceDiscipline.get_discipline()[1].getProfesor() == "Gabi"
        
    def test_sterge_disciplina(self):
        """ 
            Functie de test pentru stergere_disciplina
        """
        self.serviceDiscipline.reset_list()
        self.serviceDiscipline.adauga_disciplina(12 , "Mate", "Stefan")
        self.serviceDiscipline.adauga_disciplina(24 , "Info", "Daniela")
        self.serviceDiscipline.sterge_disciplina("12")
        assert self.serviceDiscipline.get_discipline()[0].getID() == 24
        assert self.serviceDiscipline.get_discipline()[0].getNume() == "Info"
        assert self.serviceDiscipline.get_discipline()[0].getProfesor() == "Daniela"
        
    def test_all(self):
        """ 
            Functie de test pentru toate functiile de test
        """
        self.test_adauga_disciplina()
        self.test_update_disciplina()
        self.test_sterge_disciplina()