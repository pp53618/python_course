# -*- coding: utf-8 -*-
name = 'sas'

for character in name:
    print(character)

# %%
name = 'python'
index = 0

for character in name:
    print(index, character)
    index = index + 1

# %%
for index in range(10):
    print(index)

# %%
for index in range(len(name)):
    print('Nr indeksu: ', index,'Liter: ',name[index])

# %%
for i in enumerate(name):
    print(i)

# %%
for index, character in enumerate(name):
    print(index, character)

# %%
for i, value in enumerate([4, 5, 6, 7, 8]):
    print(i, value)

# %%
for i in range(10, 20):
    print(i)

# %%
for i in range(10, 20, 2):
    print(i)

# %%
for i in range(10, -1, -1):
    print(i)

# %%
for i in range(10, 100, 10):
    print(i)

# %%
techs = 'java'
for i in range(len(techs)):
    print(i, techs[i])

# %%
string = 'Python course'
for char in string[:6]:
    print(char)

# %%
string = 'Python course'
for char in string[::-1]:
    print(char)

# %%
hastags = '#sport#gym#fitnes'
for char in hastags:
    print(char)

# %%
hastags = '#sport#gym#fitnes'
for char in hastags:
    if char not in '#':
        print(char)

# %%
for char in zip('abcde', '12345'):
    print(char)

# %%
for char, number in zip('abcde', 'python'):
    print(char, number)

# %%
hastags = '#sport#gym#fitnes#'

result =''
for char in hastags:
    if char not in '#':
        result = result + char
    else:
        print(result)
        result = ''










