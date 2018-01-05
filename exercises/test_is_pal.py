from is_palindrome_ans import is_pal

def test(word, result):
    '''
    s -> string
    result -> boolian
    '''
    if is_pal(word) == result:
        return "Correcte"
    else:
        return "Not Correcte"

print('The test case: "a", and your answer is -> ', end="")
print(test('a', True))
print('The test case: "aa", and your answer is -> ', end="")
print(test('aa', True))
print('The test case: "aA", and your answer is -> ', end="")
print(test('aA', True))
print('The test case: "abcba", and your answer is -> ', end="")
print(test('abcba', True))
print('The test case: "abccba", and your answer is -> ', end="")
print(test('abccba', True))
print('The test case: "abcCBA", and your answer is -> ', end="")
print(test('abcCBA', True))
print('The test case: "ab", and your answer is -> ', end="")
print(test('ab', False))
print('The test case: the empty string, and your answer is -> ', end="")
print(test('', False))
