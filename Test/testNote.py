import unittest

class TestNote(unittest.TestCase):
    
    def __init__(self, serviceNote, serviceStudent, serviceDiscipline):
        """ 
            Functie de initiere pentru modulul de teste Note
        """
        self.serviceNote = serviceNote
        self.serviceStudenti = serviceStudent
        self.serviceDiscipline = serviceDiscipline
        self.tearDown()
        
    def tearDown(self):
        """  
            Functie de resetare a testelor
        """
        self.serviceStudenti.reset_list()
        self.serviceNote.reset_list()
        self.serviceDiscipline.reset_list()
        
    def test_adauga_nota(self):
        
        self.serviceStudenti.adauga_student(48 , "Tudor", 19)
        
        self.serviceDiscipline.adauga_disciplina(12 , "Mate", "Stefan")
        
        self.serviceNote.adauga_nota(23 , 10, 48 , 12)
        self.serviceNote.adauga_nota(45 , 7, 48 , 12)
        
        self.assertTrue( self.serviceNote.get_note()[1].getStudent().getNume() == "Tudor")
        self.assertTrue( self.serviceNote.get_note()[1].getDisciplina().getNume() == "Mate")
        self.assertTrue( self.serviceNote.get_note()[1].getValoare() == 7)
        self.assertTrue( self.serviceNote.get_note()[1].getID() == 45)
        self.tearDown()
        
    def test_sterge_nota(self):
        self.serviceStudenti.adauga_student(48 , "Tudor", 19)
        self.serviceDiscipline.adauga_disciplina(12 , "Mate", "Stefan")
        
        self.serviceNote.adauga_nota(23 , 10, 48 , 12)
        self.serviceNote.adauga_nota(45 , 7, 48 , 12)
        
        self.serviceNote.sterge_nota(23)
        
        self.assertTrue( self.serviceNote.get_note()[0].getStudent().getNume() == "Tudor")
        self.assertTrue( self.serviceNote.get_note()[0].getDisciplina().getNume() == "Mate")
        self.assertTrue( self.serviceNote.get_note()[0].getValoare() == 7)
        self.assertTrue( self.serviceNote.get_note()[0].getID() == 45)
        self.tearDown()
        
    def test_filt_nume_nota(self):
        """
            Test filt_nume_nota
        """
        self.serviceStudenti.adauga_student(48 , "Tudor", 19)
        self.serviceStudenti.adauga_student(56 , "Dragos", 19)
        self.serviceStudenti.adauga_student(13 , "Adi", 19)
        
        self.serviceDiscipline.adauga_disciplina(12 , "Mate", "Stefan")
        
        self.serviceNote.adauga_nota(23 , 10, 48 , 12)
        self.serviceNote.adauga_nota(3 , 9, 56 , 12)
        self.serviceNote.adauga_nota(5 , 8, 13 , 12)
        self.serviceNote.adauga_nota(45 , 7, 48 , 12)
        
        lista = self.serviceNote.filtrare_nume_nota("Mate")
        
        self.assertTrue( lista[0].getStudent().getNume() == "Adi")
        self.assertTrue( lista[1].getStudent().getNume() == "Dragos")
        self.assertTrue( lista[2].getStudent().getNume() == "Tudor")
        self.tearDown()
        
    def test_filt_nota_nume(self):
        """
            Test filt_nota_nume
        """
        self.serviceStudenti.adauga_student(48 , "Tudor", 19)
        self.serviceStudenti.adauga_student(56 , "Dragos", 19)
        self.serviceStudenti.adauga_student(13 , "Adi", 19)
        
        self.serviceDiscipline.adauga_disciplina(12 , "Mate", "Stefan")
        
        self.serviceNote.adauga_nota(1 , 10, 48 , 12)
        self.serviceNote.adauga_nota(2 , 9, 56 , 12)
        self.serviceNote.adauga_nota(3 , 8, 13 , 12)
        self.serviceNote.adauga_nota(4 , 10, 48 , 12)
    
        lista = self.serviceNote.filtrare_nota_nume("Mate")
        
        self.assertTrue( lista[3].getStudent().getNume() == "Adi")
        self.assertTrue( lista[2].getStudent().getNume() == "Dragos")
        self.assertTrue( lista[0].getStudent().getNume() == "Tudor")
        
        self.tearDown()
        
    def test_filt_20(self):
        """
            Test filt_20
        """
        self.serviceStudenti.adauga_student(1 , "Tudor", 19)
        self.serviceStudenti.adauga_student(2 , "Dragos", 19)
        self.serviceStudenti.adauga_student(3 , "Adi", 19)
        self.serviceStudenti.adauga_student(4 , "Guta", 19)
        self.serviceStudenti.adauga_student(5 , "Gaboru", 19)
        
        self.serviceDiscipline.adauga_disciplina(1 , "Mate", "Stefan")
        self.serviceDiscipline.adauga_disciplina(2 , "Info", "Daniela")

        self.serviceNote.adauga_nota(1 , 10, 1 , 1)
        self.serviceNote.adauga_nota(2 , 9 , 1 , 2)
        self.serviceNote.adauga_nota(3 , 10 , 1 , 2)
        
        self.serviceNote.adauga_nota(4 , 9, 2 , 1)
        self.serviceNote.adauga_nota(5 , 9, 2 , 2)
        self.serviceNote.adauga_nota(6 , 7, 2 , 2)
        
        self.serviceNote.adauga_nota(7 , 8, 3 , 1)
        self.serviceNote.adauga_nota(8 , 9, 3 , 2)
        self.serviceNote.adauga_nota(9 , 6, 3 , 2)
        
        self.serviceNote.adauga_nota(10 , 8, 4 , 2)
        self.serviceNote.adauga_nota(11, 10, 4 , 2)
        self.serviceNote.adauga_nota(12 , 10, 4 , 2)
        
        self.serviceNote.adauga_nota(13 , 6, 5 , 2)
        self.serviceNote.adauga_nota(14, 8, 5 , 2)
        self.serviceNote.adauga_nota(15, 7, 5 , 2)
        
        lista = self.serviceNote.filtrare_20()
        
        self.assertTrue( lista[0].getNume() == "Tudor")
        self.assertTrue( not len(lista) == 2)
        self.tearDown()
            
    
    def test_all(self):
        """ 
            Functie de test pentru toate functiile de test
        """
        self.test_adauga_nota()
        self.test_sterge_nota()
        self.test_filt_nume_nota()
        self.test_filt_20()
        self.test_filt_nota_nume()
