# -*- coding: utf-8 -*-

hastags = '#weekend#good#time#'

result =''
for char in hastags:
    if char not in '#':
        result = result + char
    else:
        if result:
            print(result)
            result = ''
