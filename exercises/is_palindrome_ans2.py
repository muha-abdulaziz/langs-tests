def isPalindrome(s):
    '''Assumes s is an str
       Returns True if s is a palindrome; False otherwise.
       punctuation marks, blanks, and capitalization are
       ignored.'''

   def toChars(s):
       s = s.lower()
       ans = ''
       for c in s:
           if c in 'abcdefghijklmnopqrstuvwxyz':
               ans = ans + c
       return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))