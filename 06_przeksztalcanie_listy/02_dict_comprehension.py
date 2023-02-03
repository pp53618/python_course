# -*- coding: utf-8 -*-

stocks = {'AMZN.US': 'Amazon.com Inc', 'GOOGL.US': 'Alphabet Inc',
          'AAPL.US': 'Aplle Inc', 'UBER.US': 'Uber Technologies Inc', 
          'MSFT.US': 'Microsoft Corp'}

# %%
stocks.keys()
stocks.values()
stocks.items()

for key, value in stocks.items():
    print('{:8}: {}'.format(key, value))

#%%
stocks_dict = {key:value for (key, value) in stocks.items()}

# %%
stocks_set = {(key, value) for (key, value) in stocks.items()}

# %% zamiana key na value i value na key
stock_invert = {value:key for (key, value) in stocks.items()}

# %% Zmienjszenie literek na małe
stocks_lower = {key.lower():value for (key, value) in stocks.items()}

# %%
stocks_lenght = {key:len(value) for (key, value) in stocks.items()}

# %%
s_l = {k:v + ':' + str(len(v)) for (k, v) in stocks.items()}

# %%
def replace_corp_inc(name):
    name = name.replace('Corp', '0')
    name = name.replace('Inc', '1')
    return name

stock_flag = {k:replace_corp_inc(v) for (k, v) in stocks.items()}

# %%
stocks_corp = {k:v for (k, v) in stocks.items() if 'Corp' in v}
stocks_inc = {k:v for (k, v) in stocks.items() if 'Inc' in v}

# %%
stocks_A = {key:value for (key, value) in stocks.items() \
            if value.startswith('A') if len(value) < 13}

# %% cz.2
stocks = {'AMZN.US': 'Amazon.com Inc', 'GOOGL.US': 'Alphabet Inc',
          'AAPL.US': 'Aplle Inc', 'UBER.US': 'Uber Technologies Inc', 
          'MSFT.US': 'Microsoft Corp'}

{key: 'Corp' if 'Corp' in val else 'Inc' for (key, val) in stocks.items()}

# %%
numbers = range(20)
numbers_dict = {}

for n in numbers:
    if n % 2 == 0:
        numbers_dict[n] = n ** 2

print(numbers_dict)

# %%
numbers_dict = {key: key ** 2 for key in numbers if key % 2 == 0}

# %%
nested_dict = {'001': {'price': 100},
               '002': {'price': 40}, 
               '003': {'price': 60}}

for key, val in nested_dict.items():
    print(key, val)

# %%
{key:val['price'] for (key, val) in nested_dict.items()}

# %%
nested_dict = {'001': {'price': 100, 'items': 4},
               '002': {'price': 40, 'items': 9}, 
               '003': {'price': 60, 'items': 8}}

# %%
for key, val in nested_dict.items():
    print(key, val)

# %%
{key:val['price'] for (key, val) in nested_dict.items()}
{key:val['price'] * val['items'] for (key, val) in nested_dict.items()}



