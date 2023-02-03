# -*- coding: utf-8 -*-

capitals = {'Polska':'Warszawa', 'Niemcy':'Berlin', 'Czechy':'Praga'}
capitals['Włochy'] = 'Rzym'

capitals_copied = capitals.copy()

cities = sorted(list(capitals_copied.values()))
print(cities)

