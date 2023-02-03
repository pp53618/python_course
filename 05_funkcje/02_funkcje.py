# -*- coding: utf-8 -*-

def funkcja_1():
    print('Pierwsza funkcja uruchomiona.')

funkcja_1()

# %%
def funkcja_2(x, y=10):
    print('Podane argumanty to: y={1}, x={0}'.format(x, y))

funkcja_2(2, y=5)

# %%
import math

math.sqrt(9)
math.exp(1)
math.sin(0)

# %%
def funkcja_3():
    print('Uruchomiono.')

funkcja_3()
print(type(funkcja_3))    

fun = funkcja_3()

# %%
def add(x, y):
    return x + y

result = add(2 , 6)

# %%
def subtract (x: int, y: int):
    """"
    Odejmuje od siebie dwie liczby.
    """
    return x - y

subtract(10, 6)

# %%
def print_menu():
    print('Start programu...')
    print('*' * 30)
    print("""Wybierz jedną z podanych opcji:
          0 - logowanie
          1 - wyjscie""")
    print('*' * 30)
    print('Koniec programu.')

print_menu()

# %%
def print_even(maximum):
    even = []
    for i in range(maximum + 1):
        if i % 2 == 0:
            even.append(i)
    return even        

print_even(10)
num = print_even(20)

# %%
def write_file(file_name, text):
    with open(file_name, 'w') as file:
        print(text, file=file)
        
write_file('sample.txt', 'Pierwsza linia.\nDruga linia.')
write_file('sample2.txt', 'Pierwsza linia.\nDruga.\nTrzecia')

# %%
def calculate_profit(pv=1000, rate=0.03, n=1):
    return pv * (1 + rate)**n - pv

#calculate_profit(1000, 0.02, 1)
calculate_profit(rate=0.2)



