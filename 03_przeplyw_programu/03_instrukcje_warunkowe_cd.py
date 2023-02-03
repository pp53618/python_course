# -*- coding: utf-8 -*-

print('Program uruchomiony...')
print("""Wł,am się do systemu, zgadując dwucyfrowy pin.
      Numer pin składa się z cyfr: 0, 1, 2.""")
pin = input('Wprowadź numer pin: ')

if pin == '21':
    print('Brawo! złamałes system.')
elif pin == '20':
    print('Byłes blisko')
else:
    print('Nie zgadłes.')

# %%
pin = int(input('Wprowadź numer pin: '))
# print(pin)
# print(type(pin))

if pin == 21:
    print('Brawo! złamałes system.')
elif pin == 20:
    print('Byłes blisko')
else:
    print('Nie zgadłes.')

# %%
bool(0)

# %%
string = ' '

if string:
    print('Niepusty ciąg znaków')
else:
    print('Pusty ciąg znaków')    

# %%
number = 0

if number:
    print('Liczba niezerowa!')
else:
    print('Zerrrrroooo !!')    

# %%
default_flag = False

if default_flag:
    print('Doszło do defaultu')
else:
    print('Nie doszło')

# %%
default_flag = True

if not default_flag:
    print('Nie doszło')
else:
    print('Doszło do defaultu')

# %%
saldo = 10000
klient_zwerefikowany = True

if saldo > 0 and klient_zwerefikowany:
    print('Możesz wypłacić gotówkę.')
else:
    print('Nie możesz wypłacić gotówki.')

# %%
saldo = 10000
klient_zwerefikowany = True
amount = int(input('Ile chcesz wypłacić gotówki: '))


if saldo > 0 and klient_zwerefikowany and (saldo - amount) >= 0:
    print('Możesz wypłacić gotówkę.')
else:
    print('Nie możesz wypłacić gotówki.'
          'Brak wystarczającej kwoty {}'.format(abs(saldo - amount)))

# %% sprawdzenie czy p jest w tekscie python

name = 'python'

if 'p' in name:
    print('Znaleziono p')
else:
    print('Nie znaleziono p')

# %%
tech = 'python'
if tech == 'python':
    flag = 'Dobry wybór'
else:
    flag = 'Poszukaj czegos lepszego'    

# %%
# x if [warunek] else y
tech = 'python'
flag = 'Dobry wybór' if tech == 'python' else 'Poszukaj czego lepszego'





















