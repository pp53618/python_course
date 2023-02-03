# -*- coding: utf-8 -*-

# %%
1 / 0

# %%
4 + '4'

# %%
int('f')

# %%
float('sd')

# %%
try:
    1 / 0
except:
    print('nie dzieli się przez zero!')

# %%
try:
    1 / 0
except ZeroDivisionError:
    print('nie dzieli się przez zero!')
except TypeError:
    print('Zły typ.')

# %%
try:
    4 + '4'
except TypeError:
    print('Nie można dodawać tekstu do liczby.')

# %%
try:
    int('sd')
except ValueError:
    print('Zły tekst')

# %%
while True:
    x = int(input('Podaj liczbę: '))
    break

# %%
while True:
    try:
        x = int(input('Podaj liczbę: '))
        break
    except ValueError:
        print('Nie wprowadziłes poprawnej wartosci.')
        
# %%
try:
   with open('test.txt', 'r') as file:
      for line in file:
         print(line)
except FileNotFoundError:
    print('Plik nie istnieje')

# %%
raise TypeError('Błąd.')

# %%
raise ValueError('Błąd wartosci.')

# %%
def divide(x, y):
    try:
        x = int(x)
        y = int(y)
        return x / y
    except ZeroDivisionError:
        print('Dzielenie przez zero.')
    except ValueError:
         print('Musisz wprowadzić liczbę.')

#divide(3, 0)
##divide('1', '2')
divide('1', 'asad')










