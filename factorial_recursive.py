# 9! = 9 * 8 ... * 1
# 9 * 8!

def factorial(num):
    if (num == 0) or (num == 1):
        return 1

    return num * factorial(num - 1)

print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))