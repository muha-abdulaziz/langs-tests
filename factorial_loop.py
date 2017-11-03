# 9! =  9 * 8 * 7 ..... 1 = 
# 1! = 1

def factorial(num):
    if num == 0:
        print("num 0 has no factorial.")
    else:
        res = 1
        for i in range(num, 1, -1):
            res *= i
        return res

print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))

# num= 3;
# res= 1;
# for(i = num; i > 0; i++)
# do
#     res *= i;
# done