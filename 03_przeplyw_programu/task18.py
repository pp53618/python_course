# -*- coding: utf-8 -*-

fakt = 'python jest łatwy i przyjemny'
characters = list(fakt)
length = len(set(characters))

if length < 20:
    print("Mniej niż 20 unikalnych znaków.")
else:
    print("Liczba unikalnych znaków jest większa lub równa 20.")


