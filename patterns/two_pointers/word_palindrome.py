def  words_palindrome_one(s, t):
    return s.lower() == t.lower()[::-1]



def words_palindrome_three(s, t):   
    if len(s) != len(t):
        return False
    
    left = 0
    right = len(s)-1

    while left < len(s) : #or left <= right
        if  s[left].lower() != t[right].lower():
            return False
        else:
            left+=1
            right-=1
    return True
# time complexity: O(n)
# space 0(1)



print(words_palindrome_three("live", "evil"))   # True
print(words_palindrome_three("Hello", "olleh")) # True
print(words_palindrome_three("abc", "cba"))     # True
print(words_palindrome_three("abc", "bca"))  # false
