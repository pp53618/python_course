# -*- coding: utf-8 -*-

i = 0
while i < 5:
    print(i)
    i += 1

# %%
n = 0

while True:
    print(n)
    if n >= 10:
        break
    n += 1

# %%
while True:
    name = input('Podaj swoje imie: ')
    if len(name) >= 3 and name.isalpha():
        break
print('Czesc {}'.format(name))

# %%
n = 0

while n < 20:
    n += 1
    if n % 2 == 0:
        continue
    print(n)

# %%
n = 0

while n < 20:
    n += 1
    if n % 2 != 0:
        continue
    print(n)

# %%
lista_do_przeszukania = [12, 53, 13, 63, 34]
flaga = False

idx = 0
while idx < len(lista_do_przeszukania):
    idx += 1

# %%
lista_do_przeszukania = [12, 53, 13, 63, 34]
flaga = False
wartosc = 63

idx = 0
while idx < len(lista_do_przeszukania):
    if lista_do_przeszukania[idx] == wartosc:
        flaga = True
        break
    idx += 1
if flaga:
    print('Znaleziono element {}'.format(wartosc))

# %%
lista_do_przeszukania = [12, 53, 13, 63, 34]
flaga = False
wartosc = 60

idx = 0
while idx < len(lista_do_przeszukania):
    if lista_do_przeszukania[idx] == wartosc:
        flaga = True
        break
    idx += 1
if not flaga:
    lista_do_przeszukania.append(wartosc)











