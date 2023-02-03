# -*- coding: utf-8 -*-

numbers = [23, 12, 53, 13, 65, 1, 45]
wartosc = 13

idx = 0
while idx < len(numbers):
    if numbers[idx] == wartosc:
        flaga = True
        break
    idx += 1
if flaga:
    print('Znaleziono element {}'.format(wartosc))

# %%
numbers = [23, 12, 53, 13, 65, 1, 45]
i = 0

while i < len(numbers):
    if numbers[i] == 13:
        print('Znaleziono')
        break
    i += 1

