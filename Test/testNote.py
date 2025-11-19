class TestNote:
    
    def __init__(self, serviceNote, serviceStudent, serviceDiscipline):
        """ 
            Functie de initiere pentru modulul de teste Note
        """
        self.serviceNote = serviceNote
        self.serviceStudenti = serviceStudent
        self.serviceDiscipline = serviceDiscipline
        
    def test_adauga_nota(self):
        self.serviceStudenti.reset_list()
        self.serviceStudenti.adauga_student(48 , "Tudor", 19)
        self.serviceDiscipline.reset_list()
        self.serviceDiscipline.adauga_disciplina(12 , "Mate", "Stefan")
        
        self.serviceNote.adauga_nota(23 , 10, 48 , 12)
        self.serviceNote.adauga_nota(45 , 7, 48 , 12)
        
        assert self.serviceNote.get_note()[1].getStudent().getNume() == "Tudor"
        assert self.serviceNote.get_note()[1].getDisciplina().getNume() == "Mate"
        assert self.serviceNote.get_note()[1].getValoare() == 7
        assert self.serviceNote.get_note()[1].getID() == 45
        
    def test_sterge_nota(self):
        self.serviceStudenti.reset_list()
        self.serviceStudenti.adauga_student(48 , "Tudor", 19)
        self.serviceDiscipline.reset_list()
        self.serviceDiscipline.adauga_disciplina(12 , "Mate", "Stefan")
        
        self.serviceNote.adauga_nota(23 , 10, 48 , 12)
        self.serviceNote.adauga_nota(45 , 7, 48 , 12)
        
        self.serviceNote.sterge_nota(23)
        
        assert self.serviceNote.get_note()[0].getStudent().getNume() == "Tudor"
        assert self.serviceNote.get_note()[0].getDisciplina().getNume() == "Mate"
        assert self.serviceNote.get_note()[0].getValoare() == 7
        assert self.serviceNote.get_note()[0].getID() == 45
    
    def test_all(self):
        """ 
            Functie de test pentru toate functiile de test
        """
        self.test_adauga_nota()
        self.test_sterge_nota()
