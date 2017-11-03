x = int(input('Enter an integer: '))

for ans in range(0, abs(x)+1):
    if ans ** 3 == abs(x):
        break

if ans ** 3 != abs(x):
    print(x, "is not a perfect square.")
else:
    if x < 0:
        ans = -ans
    print('Cube root of ' + str(x) + ' is ' + str(ans))