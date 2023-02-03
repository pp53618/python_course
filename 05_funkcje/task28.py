# -*- coding: utf-8 -*-
def print_even(maximum):
    even = []
    for i in range(maximum + 1):
        if i % 2 != 0:
            even.append(i)
    return even        

print_even(10)
num = print_even(20)

# %%
def drukuj_nieparzyste():
    wynik = []
    for i in range(20):
        if i % 2 != 0:
            wynik.append(i)
    return wynik

# drukuj_nieparzyste()