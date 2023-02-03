# -*- coding: utf-8 -*-
# zacznij od instrukcji warunkowej, która sprawdzi czy długosc hasła jest poprawna
# następnie przejdz do sprawdzenia warunku drugiego wykorzystując pętle i instrukcje break

ps = 'jhafatys!vd'

if len(ps) > 10:
    for i in ps:
        if '!' in ps:
            print('Hasło poprawne')
            break
    else:
        print('Hasło niepoprawne')
else:
    print('Hasło niepoprawne')








