# -*- coding: utf-8 -*-

empty_list = list()
print(empty_list)

# %%
techs = ['python', 'java', 'c++', 'go', 'sql']
techs[0] = 'python 3.7'
print(techs)

# %%
numbers = [3, 4, 3, 5, 24]
print(numbers)
print(type(numbers))

# %%
mixed = ['python', 3.7, 4, True]
print(mixed)

# %%
empty = []
nested = [[1, 2, [3, 'sql']], ['python', 'java', 'go'], 3]

# %%
first = ['mleko', 'ziemniaki', 'makaron']
second = ['woda', 'jajka']

bucket = [first, second]

# %%
len(bucket)

# %%
techs = first + second + ['scala']

techs += ['javascript']
print(techs)

# %%
print(dir(list))








