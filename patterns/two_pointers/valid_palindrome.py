
import re
def valid_palindrome(s):
    s = re.sub(r'[^a-z0-9]', '', s.lower())
    print(s)
    left = 0
    right = len(s)-1
    while left < right:
        if s[left] != s[right]:
            return False
        else:
            left+=1
            right-=1
    return True

print(valid_palindrome("A man, a plan, a canal: Panama"))  # True
print(valid_palindrome("race a car"))                      # False
print(valid_palindrome("No 'x' in Nixon"))                 # True
