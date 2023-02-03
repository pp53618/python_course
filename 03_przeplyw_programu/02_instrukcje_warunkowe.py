# -*- coding: utf-8 -*-

version = 3.7
print(version)

# %%
version > 3
version <= 3

# %%
number = 1200
number > 1000

number == 1200
number == 1000

number != 1200
number != 1000

# %%
#if [warunek]:
#    [instrukcje]

# %%
if 8 > 10:
    print('Tak')
    
# %%
a = 8
if a > 10:
    print('a > 10')    
    
# %%
a = 5
if a > 10:
    print('a > 10') 
else:
    print('a <= 10')

# %%
age = 18

if age < 18:
    print('Nie masz uprawnień.')
else:
    print('Dostę przyznany.')    

# %%
age = 35
if age == 18:
    print('Masz 18 Lat')
elif age < 18:
    print('Nie masz uprawnień')
#elif age > 18:
#    print('Dostęp przyznano')
else:
    print('Dostęp przyznany')

# %%
# %%
age = int(input('Podaj swoj wiek: '))
if age == 18:
    print('Masz 18 Lat')
elif age < 18:
    print('Nie masz uprawnień')
elif age > 18:
    print('Dostęp przyznano')























