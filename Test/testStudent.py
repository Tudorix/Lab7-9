import unittest

class TestStudent(unittest.TestCase):
    
    def __init__(self, serviceStudenti):
        """ 
            Functie de initiere pentru modulul de teste alocat Student
        """
        self.serviceStudenti = serviceStudenti
        self.serviceStudenti.reset_list()
        
    def tearDown(self):
        """  
            Functie de resetare a testelor
        """
        self.serviceStudenti.reset_list()
    
    def test_adauga_student(self):
        """ 
            Functie de test pentru adauga_student
        """
        self.serviceStudenti.adauga_student(48 , "Tudor", 19)
        self.assertTrue(self.serviceStudenti.get_studenti()[0].getNume() == "Tudor")
        self.assertTrue(self.serviceStudenti.get_studenti()[0].getID() == 48)
        self.assertTrue(self.serviceStudenti.get_studenti()[0].getVarsta() == 19)
        self.serviceStudenti.adauga_student(56 , "Andrei", 23)
        self.assertTrue(self.serviceStudenti.get_studenti()[1].getNume() == "Andrei")
        self.assertTrue(self.serviceStudenti.get_studenti()[1].getID() == 56)
        self.assertTrue(self.serviceStudenti.get_studenti()[1].getVarsta() == 23)
        
        with self.assertRaises(IndexError):
            self.serviceStudenti.adauga_student(48 , "Tudor", 19)
            self.serviceStudenti.adauga_student(56 , "Erick", 19)
            
        self.tearDown()
        
    def test_update_student(self):
        """ 
            Functie de test pentru update_student
        """
        self.serviceStudenti.adauga_student(48 , "Tudor", 19)
        self.serviceStudenti.adauga_student(56 , "Andrei", 23)
        self.serviceStudenti.update_student("56", 36, "Stefan", 18)
        print(self.serviceStudenti.get_studenti()[1].getNume())
        self.assertTrue(self.serviceStudenti.get_studenti()[1].getNume() == "Stefan")
        self.assertTrue(self.serviceStudenti.get_studenti()[1].getID() == 36)
        self.assertTrue(self.serviceStudenti.get_studenti()[1].getVarsta() == 18)
        
        self.tearDown()
        
    def test_stergere_student(self):
        """ 
            Functie de test pentru stergere_student
        """
        self.serviceStudenti.adauga_student(48 , "Tudor", 19)
        self.serviceStudenti.adauga_student(56 , "Andrei", 23)
        self.serviceStudenti.sterge_student(48)
        self.assertTrue( self.serviceStudenti.get_studenti()[0].getNume() == "Andrei")
        self.assertTrue( self.serviceStudenti.get_studenti()[0].getID() == 56)
        self.assertTrue( self.serviceStudenti.get_studenti()[0].getVarsta() == 23)
        
        self.tearDown()
        
    def test_cauta_student(self):
        """ 
            Functie de test pentru cauta_student
        """
        self.serviceStudenti.adauga_student(48 , "Tudor", 19)
        self.serviceStudenti.adauga_student(56 , "Andrei", 23)
        argumente = ["ID" , 48]
        student = self.serviceStudenti.cautare_student(argumente)[0]
        self.assertTrue( student.getNume() == "Tudor")
        self.assertTrue( student.getID() == 48)
        self.assertTrue( student.getVarsta() == 19)
        
        self.tearDown()
        
    def test_gen_random(self):
        """ 
            Functie de test pentru cauta_student
        """
        self.serviceStudenti.gen_studenti(48)
        self.assertTrue( self.serviceStudenti.lenght() == 48)
        self.serviceStudenti.gen_studenti(12)
        self.assertTrue( self.serviceStudenti.lenght() == 60)
        
        self.tearDown()

    def test_filt_varsta(self):
        """ 
            Functie de test pentru filt_varsta
        """
        self.serviceStudenti.adauga_student(48 , "Tudor", 19)
        self.serviceStudenti.adauga_student(56 , "Andrei", 23)
        self.serviceStudenti.adauga_student(32 , "Stefan", 18)
        
        lista = self.serviceStudenti.filt_varsta(20)
        
        self.assertTrue( lista[0].getNume() == "Tudor")
        self.assertTrue( lista[0].getVarsta() == 19)
        self.assertTrue( lista[1].getVarsta() == 18)
        self.assertTrue( len(lista) == 2)
        
        self.tearDown()

    def test_all(self):
        """ 
            Functie de test pentru toate functiile de test
        """
        self.test_adauga_student()
        self.test_update_student()
        self.test_stergere_student()
        self.test_cauta_student()
        self.test_gen_random()
        self.test_filt_varsta()

if __name__ == '__main__':
    unittest.main()