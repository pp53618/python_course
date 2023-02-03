# -*- coding: utf-8 -*-

abs(10)
print(abs(-10))

# %%
bool([])
bool('')
bool({})
bool(' ')
bool(True)
bool(False)
bool(12)
bool(0)

# %%
dir(list)
dir(tuple)

# %%
list(enumerate(['pawel', 'python', 'java']))

# %%
eval('1 + 1') 

x = 10
eval('x + 13')

# %%
list(filter(abs, [-2, -1, 0, 1, 2]))

# %%
list(filter(bool, ['python', '', 'Java']))

# %%
float(1)
float(1.3)
float('1')
float('jhygj')

# %%
type(1)
type('dsd')

# %%
# help()
help(float)
help(int)

# %%
# isinstance?
isinstance(1, int)
isinstance(1, float)
isinstance(1.0, float)
isinstance('fghtft', str)
isinstance('', str)

# %%
len('python')
len('')
len(' ')
len([])
len([[3, 4], [3, 5], [3, 4, [6, 1]]])

# %%
list('python')
list(range(10))

# %%
list(map(abs, [-1, -2, 0, 4, 5]))

# %%
names = ['pawel', 'bartek', 'janek']
list(map(str.title, names))

# %%
max([1, 2, 3, 5])
max('pawel')
max('bartek')

min([1, 2, 3, 5])
min('pawel')

# %%
pow(2, 4)
2 ** 4

# %%
list(reversed([4, 5, 6]))
list(reversed('python'))

# %%
round(3.4143564, 2)

# %%
str(1)
str(324.24)

# %%
sum([3, 4, 5, 6])

# %%
lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6, 7]

list(zip(lista_1, lista_2))

# %%
list(zip('python', 'coursejygjfhdgrd'))








