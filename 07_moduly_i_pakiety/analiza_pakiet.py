# -*- coding: utf-8 -*-

import rocket.data

# %%
dir(rocket.data)

# %%
dane = rocket.data.get_data()

# %%
import rocket.algorytmy 

# %%
dir(rocket.algorytmy)

rocket.algorytmy.drzewa_decyzyjne()

# %% bardziej wymagany kod i ładniejszy :) 
from rocket.algorytmy import drzewa_decyzyjne

# %%
drzewa_decyzyjne()

# %%
from rocket.funkcje.stats import mean

# %%
mean(dane)

































