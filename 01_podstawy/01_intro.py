# -*- coding: utf-8 -*-

# komentarz

# %%
print(2 + 2)

# %%
print(3 * 3)

# %%
print(3 + 2 * 2)
print(4 - 2 * 2)

# %%
10 / 3
4 / 2  

# %%
10 // 3
7 // 6

# %% 
2 ** 5

# %%
10 % 3
12 % 5
11 % 2

# %%
(10 - 2 ** 3) * 10

# %%
a = 10
b = 20

c = a * b
print(c)

# %%
print('love python')
"love python"

# %%
print("It's the best")

# %%
print('It\'s the best')

# %%
print('Python 3.8')

# %%
print('Python\n3.8')

# %%
print("""Python
3.8""")

# %%
print('\tPython')
print('\t\t\tPython')

# %%
print('C:\path\to\something\new')
print('C:\path\\to\something\\new')

# %%
print(r'C:\path\to\something\new')
print('C:\\path\\to\\something\\new')

# %%
import os
os.getcwd()

# %%
print("""Instrukcja uruchamiania pliku przyklad.py:
      
      --file [nazwa pliku]
          zapisuje output do pliku
          
      --quiet
          wycisza logi w konsoli
          
Koniec.""")

# %%
text = 'I love Python. '
# print(text)
print(text * 3)
print('hau..' * 10)
print('-' * 30)

# %%
'Python'
'Py' 'thon'
'Py' ' thon'
print('Py' 'thon')

# %%
url = 'https://login.microsoftonline.com/m365ht.onmicrosoft.com/oauth2/v2.0/authorize?redirect_uri=https%3A%2F%2Fportal.azure.com%2Fsignin%2Findex%2F&response_type=code%20id_token&scope=https%3A%2F%2Fmanagement.core.windows.net%2F%2Fuser_impersonation%20openid%20email%20profile&state=OpenIdConnect.AuthenticationProperties%3Da8h9-kL1hWQAvqFmf8I7QuNh8qxCv6ksJbjokpNecL8FCQI7gKs0EVKopXNo6ZL6Z-BkAeGawinQRjb61t9OSSa7JvgRc-2OOjfO_jic-G2K-1UChmu3EQ0WtyGcpqj9NpMfZizDbBaUTZcDhEwJdIJpIzTgJkUc2ow4Sy6ZKkPtDzvaRiQDBR5afZJaf2AiA9qoCqVQpqb_mMQ43aaGxmO0uvojORoHladv6L3j9ufvdpmwcR2cmrGS4sDWVvl2K7-fU4uMzaFpmw7RaN13KzZ54rKH1f1KfiYja_iYeeHTG8Q98cNNi7s_s1A9Q9K6dXmM2wx7UC8xaVepkoF7WRg6yYNtbEo1SVHm85RNooRl9HO0kfooDwzfq_7Ss09Io8jzAZoN2SSg2JHz0CKtZw2MNqdMGsIlkymS0nUZkLEuacB5YmW-vXYnjTAmQv0n&response_mode=form_post&nonce=638056076069467108.YTZlYzA3YmQtNmVkNi00Yjc4LTk3YWEtN2NhYmY1NTYzNTY5NzMyMDlhZGEtZDdiOC00YmZjLThmY2YtODdmZWE0NmQ1ZjQ0&client_id=c44b4083-3bb0-49c1-b47d-974e53cbdf3c&site_id=501430&client-request-id=e670912f-d14e-4814-82a9-611be576e884&x-client-SKU=ID_NET472&x-client-ver=6.22.1.0&sso_reload=true'

url_2 = ('https://docs.cypress.io/guides/guides/'
'test-retries#docusaurus_skipToContent_fallback')

# %%
name = 'Python'
print(name + ' 3.8')
print(name, '3.8')

# %%
age = 35
imie = 'Bartek'

print(imie + ' ' + str(age))
print(imie, age)
print('{1} ma {0} lat.'.format(imie, age))

# %%
saldo = 40
# saldo = saldo + 30 to samo ale krócej można zrobić poniżej
saldo += 30
# saldo = saldo - 10
saldo -= 10
print(saldo)

# %%
lokata = 1000
czynnik_akumulacyjny = 1 + 0.04
lokata_po_roku = lokata * czynnik_akumulacyjny
print('Wartosc lokaty po rok:', lokata_po_roku)

# %%
pixel = 150
#pixel = pixel / 255
pixel /= 255
print(pixel)

# %%
base = 2
# base = base ** 5
base **= 5
print(base)

# %%
x = 103
# x = x % 10
x %= 10
print(x)

# %%
imie = 'Bartek '
nazwisko = 'Mackiewicz'
# nazwa = imie + nazwisko 
imie += nazwisko 

# %%
name = 'Python '
version = '3.8'
name += version
print(name)











