# -*- coding: utf-8 -*-

raw_data = '245!9898!97987!9809!090'
clean_data = ''

for char in raw_data:
    if char != '!':
        clean_data += char
    else:
        clean_data += ','
print(clean_data)

# %%
suma = 0
for i in range(10):
    suma += i
print(suma)

# %%
saldo = 450
print('Saldo początkowe {}'.format(saldo))
for kwota in range(10, 60, 10):
    print('Wypłacona kwota {}'.format(kwota))
    saldo -= kwota
    print('Saldo: {}'.format(saldo))
print('Saldo końcowe: {}'.format(saldo))

# %%
print('Witaj w systemie logowania.')
print('*' * 30)
nick = input('Podaj swój nick: ')
pin = input('Podaj swój pin, {}: '.format(nick))

if len(pin) == 4:
    
    for char in pin:
        if char not in '0123456789':
            print('Podałes niepoprawny kod pin.')
            break
    else:
        print('Kod pin ważny.')
else:
    print('Podałes niepoprawny kod pin.')




















