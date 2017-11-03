x = int(input('Enter an integer: '))

ans = 0
while ans ** 3 < abs(x):
    ans = ans + 1

if ans ** 3 != abs(x):
    print(x, "is not a perfect Cube.")
else:
    if x < 0:
        ans = -ans
    print('Cube root of ' + str(x) + ' is ' + str(ans))

# 0 .. x
# 0 .. n .. 27

# n ** 3

# 27 -> 3
# 9 -> 3
# 25 -> 5

