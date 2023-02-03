# -*- coding: utf-8 -*-

x = 'Programowanie w języku Python - od A do Z'
x = x.lower()
x = x.replace('ę', 'e')
x = x.replace(' ', '')
x = x.replace('-', '')

print(len(set(x)))


# %%
x = 'Programowanie w języku Python - od A do Z'
x = x.lower().replace('ę', 'e').replace(' ', '').replace('-', '')

print(len(set(x)))