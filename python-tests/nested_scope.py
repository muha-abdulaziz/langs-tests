def f(x):
    def g():
        x = 'abc'
        print('x =', x)
    
    def h():
        z = x
        print('z =', z)
    
    x = x + 1
    print('x =', x)
    h()
    g()
    print('x =', x)
    return g

x = 3
z = f(x)
print('x =', x)
print('z =', z)
z()