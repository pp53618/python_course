# -*- coding: utf-8 -*-

class Czlowiek:
    
    pochodzenie = 'Ziemia'
    imie = 'Bartek'


class Polak:
    
    kraj = 'Polska'
    imie = 'Piotr'
    
    
class Pilkarz(Czlowiek, Polak):
    
    def info(self):
        print(f'Utworzony obiekt pochodzi z planety {self.pochodzenie}.\n' 
              f'Kraj pochodzenia: {self.kraj}.\n'
              f'Nazwa obiektu: {self.imie}.')

# %%
pilkarz_1 = Pilkarz()
pilkarz_1.info()





























