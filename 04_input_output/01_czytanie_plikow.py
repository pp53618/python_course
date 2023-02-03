# -*- coding: utf-8 -*-


file = open(r'C:/Users/paula/.spyder-py3/repos/python_course/04_input_output/simple.txt')

for line in file:
    print(line, end='')

file.close()

# %%
with open(r'C:/Users/paula/.spyder-py3/repos/python_course/04_input_output/simple.txt') as file:
    for line in file:
        print(line, end='')

# %%
with open(r'C:/Users/paula/.spyder-py3/repos/python_course/04_input_output/simple.txt') as file:
    line = file.readline()
    print(line)

# %%
with open(r'C:/Users/paula/.spyder-py3/repos/python_course/04_input_output/simple.txt') as file:
    lines = file.readlines()
    print(lines)

# %%
with open(r'C:/Users/paula/.spyder-py3/repos/python_course/04_input_output/simple.txt') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')

# %%
with open(r'C:/Users/paula/.spyder-py3/repos/python_course/04_input_output/simple.txt') as file:
    line = file.readline()
    while line:
        print(line, end='')
        line = file.readline()
        
# %%
with open(r'C:/Users/paula/.spyder-py3/repos/python_course/04_input_output/simple.txt') as file:
    lines = file.read()
    print(lines)

# %%
# %%
with open(r'C:/Users/paula/.spyder-py3/repos/python_course/04_input_output/data.txt') as file:
    data = file.readlines()
    for line in data:
        print(data)






