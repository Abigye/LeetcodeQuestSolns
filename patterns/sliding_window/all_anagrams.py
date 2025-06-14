#  Find All Anagrams in a String (#438)
# Input: s = "cbaebabacd", p = "abc"

# Output: [0, 6]

from collections import Counter
def is_anagram(t,s):
    return Counter(s.lower()) == Counter(t.lower())


def find_all_anagrams(string, pattern):
    pattern_len = len(pattern)
    string_len = len(string)

    if string_len == 0 or pattern_len == 0 or string_len < pattern_len:
        return []

    first_string = string[:pattern_len]

    all_anagrams = []

    if is_anagram(first_string, pattern):
        all_anagrams.append(first_string)

    left = 0
    right = pattern_len

    curr_string = first_string.split()

    while right < string_len:
        curr_string = string[left+1 : right+1]

        print(curr_string)

        if is_anagram(curr_string, pattern):
            all_anagrams.append(curr_string)

        left+=1
        right+=1

    return all_anagrams


# print(find_all_anagrams("cbaebabacd", "abc"))


def find_all_anagrams_2(string, pattern):
    pattern_len = len(pattern)
    string_len = len(string)

    if string_len == 0 or pattern_len == 0 or string_len < pattern_len:
        return []

    anagrams = []

    left = 0
    right = pattern_len

    curr_string = ""

    while right < string_len:
    
        curr_string = string[left:right]
        print(curr_string)
   
        if Counter(curr_string.lower()) == Counter(pattern.lower()):
            anagrams.append((curr_string, left, right-1))

        left+=1
        right+=1

    return anagrams

print(find_all_anagrams_2("cbaebabacd", "abc"))
print(find_all_anagrams_2("cb", "abc"))
print(find_all_anagrams_2("", "aaa"))
print(find_all_anagrams_2("ababcdbacdcabdcccbdeee", "abcd"))









