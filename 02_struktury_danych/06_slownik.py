# -*- coding: utf-8 -*-

empty_dict = dict()
print(empty_dict)

d = {}
print(type(d))

e = set()

# %%
pol_to_eng = {'jeden':'one', 'dwa':'two', 'trzy':'three'}

name_to_digit = {'jeden':1, 'dwa':2, 'trzy':3}

# %%
name_to_digit = {0:1, 1:2, 2:3}

len(name_to_digit)

# %%
# dict = {'key1':'value1', 'key2':'value2'}

# %% Wstawianie kolejnych elementów do słownika
pol_to_eng['cztery'] = 'four'

# %%
pol_to_eng.clear()

# %%
pol_to_eng_copied = pol_to_eng.copy()

# %% Wydobywamy klucze
list(pol_to_eng.keys())

# %% Wydobywamy wartosci
list(pol_to_eng.values())

# %% Wydobywamy klucze i wartosci
list(pol_to_eng.items())

# %%
pol_to_eng['jeden']
# pol_to_eng['zero']

pol_to_eng.get('zero', 'Nan')

# %%
# pol_to_eng.pop('dwa')
pol_to_eng.popitem()

# %%
pol_to_eng.update({'dwa':2})












