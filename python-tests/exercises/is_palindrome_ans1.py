#! /usr/bin/env python3
def to_small(s):
    '''
    This function takes a string and changes all characters to small case.

    input -> string
    output -> string
    '''
    return s.lower()

def is_pal(s):
    s = to_small(s)
    if s == "":
        return False

    if len(s) == 1:
        return True
    if len(s) == 2:
        return s[0] == s[-1]

    if s [0] == s[-1]:
        return is_pal(s[1:-1])

if __name__ == '__main__':
    print("\nThis programe checks if the string is palindrome or not.")
    check_str = input("Enter a string: ")
    
    print("You entered '{}',".format(check_str), end=" ")
    if is_pal(check_str):
        print("and it is palindrome.")
    else:
        print("and it is not palindrome.")