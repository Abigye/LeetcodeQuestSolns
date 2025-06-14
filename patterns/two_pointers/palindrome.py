
def is_palindrome_one(s):
    return s == s[::-1]
# Time Complexity: O(n)
# Space Complexity: O(n) (because s[::-1] creates a new string)

print(is_palindrome_one("racecar"))
print(is_palindrome_one("hello"))


def is_palindrome_two(s):
    # using two pointers
    left = 0
    right = len(s)-1
    while left < right:
        if s[left] != s[right]:
            return False
        else:
            left+=1
            right-=1
    
    return True
# time complexity: O(n)
# space 0(1)

print(is_palindrome_two("racecar"))
print(is_palindrome_two("hello"))

    
