# -*- coding: utf-8 -*-

class Student:
    
    lista_studentow = []
    
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.lista_studentow.append(self)
     
    @classmethod
    def liczba_studentow(cls):
        print('Liczba Studentów:', len(Student.lista_studentow))

# %%
student_1 = Student('Jan', 'Kowalski', 18)
student_2 = Student('tomasz', 'Nowak', 23)
studeent_3 = Student('Jan', 'Nowak', 20)

# %%
Student.liczba_studentow()























