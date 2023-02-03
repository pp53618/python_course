# -*- coding: utf-8 -*- 
# args - może być inna nazwa ale często się pojawia

def test_args(x, *args):
    print('Pierwszy parametr: ', x)
    for arg in args:
        print('Kolejny parametr *args: ', arg)
        
test_args(4, 5, 6, 8)

# %%
def funkcj_1(x, y, *args):
    print('x=' , x)
    print('y=', y)
    print('*args=', args)

funkcj_1(1, 2)
funkcj_1(1, 2, 3)
funkcj_1(1, 2, 3, 4)

# %%
def suma(x, y):
    return x + y

def suma_dowol(*args):
    return sum(args)

# %%
suma_dowol(1, 2, 3, 4, 5, 6, 7)

# %%
def funkca_2(**kwargs):
    for kwargs in kwargs:
        print(kwargs)
        
funkca_2(**{'a': 1, 'b': 2})        

# %%
def fun(**kwargs):
    print(kwargs)
    
#fun(a=1, b=4)    
fun(x1=10, x2=20, x3=30)

# %%
def fun_2(*args, **kwargs):
    print(args)
    print(kwargs)
    
fun_2(1, 2, 3, 4, a=10, b=20)

# %%
def fun_3(*args, **kwargs):
    print(sum(args))
    print(kwargs.values())
    
fun_3(1, 2, 3, 4, a=10, b=20)












