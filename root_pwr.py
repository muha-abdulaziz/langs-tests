# Write a program that asks the user to enter an integer and points two integers
# root and pwr, such that 0 < pwr < 6 and root ** pwr is equal to the integer
# entered by the user. if no such pair of integer exists, it should print
# a message to that effect.

print("\n*****************************************************************")
print("**                                                             **")
print("** This program takes an integar number. and return 2 integers.**")
print("** root and power. such that 0 < power < 6 and                 **")
print("** root ** power = your integer number.                        **")
print("**                                                             **")
print("*****************************************************************\n")

num = int(input("Enter an integer number: "))
pwr = 1
root = 0
ok = False
while root ** pwr < num:
    print("--> root =", root)
    while pwr < 6:
        print("root =", root, "and power =", pwr)
        if root ** pwr >= num:
            ok = True
            break
        pwr += 1
    
    if ok:
        break

    root += 1
    pwr = 1

if root ** pwr == num:
    print("root =", root, "and power =", pwr)
    print(str(root) + " ** " + str(pwr) + " = " + str(num))
else:
    print("There is no root ** pwr = " + str(num) + ", such 0 < power < 6")
    print()