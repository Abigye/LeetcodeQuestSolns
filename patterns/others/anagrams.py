
from collections import Counter
def is_anagrams(s, t):
    s = s.lower()
    t = t.lower()
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t) 
