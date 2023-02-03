# -*- coding: utf-8 -*-

kwota_poczatkowa = 1000
stopa_procentowa = 0.05
okres_trwania = 2

fv = kwota_poczatkowa * (1 + stopa_procentowa) ** okres_trwania
print(fv)