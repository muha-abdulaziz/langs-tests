#! /usr/bin/env python3

def to_small(s):
    '''
    This function takes a string and changes all characters to small case.

    input -> string
    output -> string
    '''
    pass

def is_pal(s):
    '''
    This function checks if the string is palindrome
    input -> string
    output -> boolian
    '''
    # use to_small function
    pass

if __name__ == '__main__':
    print("\nThis programe checks if the string is palindrome or not.")
    check_str = input("Enter a string: ")
    
    print("You entered '{}',".format(check_str), end=" ")
    if is_pal(check_str):
        print("and it is palindrome.")
    else:
        print("and it is not palindrome.")