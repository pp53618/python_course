# -*- coding: utf-8 -*-

text = 'Witaj na kursie Pythona.\nPython jest wspaniały.'

print(text)

# %%
dir(text)
help(str.count)

# %%
text.capitalize()

# %%
text.title()

# %%
text.count('Python')

# %%
text.startswith('kurs')

# %%
'python'.startswith('py')

# %%
text.endswith('y.')

# %%
'sample.py'.endswith('.py')

# %%
'sample.png'.endswith('.png')

# %%
text.find('Python')
text[text.find('Python'):]

# %%
hashtags = 'sport#gym'
idx = hashtags.find("#")
hashtags[:idx]

# %%
'pawel1453!'.isalnum()

# %%
'3353624'.isdigit()
'3rd353624'.isdigit()

# %%
'pytHon'.islower()

'PAWEL'.isupper()

# %%
' '.join(['python', '3.8'])
'#'.join(['sport', 'gym', 'fit'])
','.join(['1', '2', '3', '4'])


# %%
'#good#time#mod'.replace('#', ' ')

# %%
'column name'.replace(' ', '_')

# %%
'    python    '.strip()
'    python    '.rstrip()
'    python    '.lstrip()

# %%

'1,2,3,4,5,6,7'.split(',')

'python java php sql sas'.split()

'#gym#fit#mod'.split('#')

# %%
'12'.zfill(5)
'1'.zfill(10)








