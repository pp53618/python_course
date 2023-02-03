# -*- coding: utf-8 -*-

empty_tuple = tuple()
print(empty_tuple)

# %%
amazon = ('Amazon', 'USA', 'Technology', 1)
google = ('Google', 'USA', 'Technology', 2)

# %%
name_google = google[0]
# google[0] = 'Google Company'

# %%
data = (amazon, google)
print(data)

# %%
a = ('Bartek', 'Mackiewicz')
print(a)

# %%
imie = 'Bartek'
nazwisko = 'Mackiewicz'

imie, nazwisko, id_user = ('Bartek', 'Mackiewicz', '001')

# %%
amazon_name, counrty, sector, rank = amazon

# %%
stock = 'Amazon', 'Apple', 'IBM'

print(type(stock))

# %%
nested = 'Europa', 'Polska', ('Warszawa', 'Kraków', 'Wrocław')
print(nested)

# %%
a = 12
b = 14

c = b
b = a
a = c
print(a, b)

# %%
x, y = 10, 15
x, y = y, x
print(x, y)






















