"""
This program finds the square root.
"""

x = int(input('Enter an integer: '))
def sqrt(x):
    '''
    This program finds the square root.
    '''
    x = x
    ans = 0

    while ans ** 2 < abs(x):
        ans = ans + 1

    if ans ** 2 != abs(x):
        print(x, "is not a perfect square.")
    else:
        if x < 0:
            ans = -ans
        
        print('Square root of ' + str(x) + ' is ' + str(ans))