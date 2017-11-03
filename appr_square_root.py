#!/usr/bin/python3
#x = int(input('Enter an integer: '))
x = int(input('Enter an integer: '))

epsilon = 0.001
step = epsilon ** 2
numGesses = 0
ans = 0.0

while abs(ans**2 - x) >= epsilon and ans <= x:
    ans += step
    numGesses += 1

print("numGesses = " + str(numGesses))
if abs(ans**2 - x) >= epsilon:
    print('Failed on square root of', x)
else:
    print(ans, "is close to square root of", x)

# 5 + (7 * n)
# 5 + 7 * 1
# 5 + 7 * 500000
# O(n)


# x = []
# for i in range(0, len(x)+1):
#     # x[1]
#     for j in range(i+1, len(x) + 1):
#         # x[]
# 10 * 10
# n ** 2

# O(log(n))
# O(n)
# O(n ** C)
# o(C ** n)

# 2 4 16 32 64 128 256 512 


# O(n * log(n))