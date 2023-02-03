# -*- coding: utf-8 -*-
files = ['run_me.py', 'README.md', 'help.txt', 'script.py', 'menu.py', 'main.py', 'py']

def generator_py(lista):
    for item in lista:
        if item.endswith('.py'):
            yield item

gen = generator_py(files)

# %%
next(gen)


