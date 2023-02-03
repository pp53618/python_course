# -*- coding: utf-8 -*-

"""
Opis metod: 
    
    unittest.skip(reason)
        pomija oznaczony test
    
    unittest.skipIf(condition, reason)
        pomija onaczony test jeżeli warunek jest prawdziwy
        
    unittest.skipUnless(condition, reason)
        pomija oznaczony test, chyba, że warunek jest prawdziwy
    
    unittest.expectedFailure()
        oznacza test jako oczekiwany błąd,
        jeżęli test będzie niepowodzeniem
        nie zostanie policzony jak błąd
    
"""

import unittest


class SimpleTest(unittest.TestCase):
    
    x = 6
    y = 8
    
    @unittest.skip('pomiń')
    def test_add(self):
        wynik = self.x + self.y
        self.assertEqual(wynik, 6)
        
    @unittest.skipIf(x < y, 'pomin')    
    def test_sub(self):
        wynik = self.x - self.y
        self.assertEqual(wynik, 4)

    @unittest.skipUnless(y == 0, 'pomiń')
    def test_div(self):
        wynik = self.x / self.y
        self.assertEqual(wynik, 3.0)

    @unittest.expectedFailure
    def test_mul(self):
        wynik = self.x * self.y
        self.assertEqual(wynik, 11)

if __name__ == '__main__':
    unittest.main()











