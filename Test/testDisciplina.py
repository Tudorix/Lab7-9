class TestDiscipline:
    
    def __init__(self, serviceDiscipline):
        self.serviceDiscipline = serviceDiscipline
        
    def test_adauga_disciplina(self):
        self.serviceDiscipline.reset_list()
        self.serviceDiscipline.adauga_disciplina(12 , "Mate", "Stefan")
        assert str(self.serviceDiscipline.get_discipline()) == "[(12 , Mate , Stefan)]"
        self.serviceDiscipline.adauga_disciplina(24 , "Info", "Daniela")
        assert str(self.serviceDiscipline.get_discipline()) == "[(12 , Mate , Stefan), (24 , Info , Daniela)]"
        
    def test_update_disciplina(self):
        self.serviceDiscipline.reset_list()
        self.serviceDiscipline.adauga_disciplina(12 , "Mate", "Stefan")
        self.serviceDiscipline.adauga_disciplina(24 , "Info", "Daniela")
        self.serviceDiscipline.update_disciplina(24,36, "FP", "Gabi")
        assert str(self.serviceDiscipline.get_discipline()) == "[(12 , Mate , Stefan), (36 , FP , Gabi)]"
        
    def test_sterge_disciplina(self):
        self.serviceDiscipline.reset_list()
        self.serviceDiscipline.adauga_disciplina(12 , "Mate", "Stefan")
        self.serviceDiscipline.adauga_disciplina(24 , "Info", "Daniela")
        self.serviceDiscipline.sterge_disciplina("24")
        assert str(self.serviceDiscipline.get_discipline()) == "[(12 , Mate , Stefan)]"
        
    def test_all(self):
        self.test_adauga_disciplina()
        self.test_update_disciplina()
        self.test_sterge_disciplina()