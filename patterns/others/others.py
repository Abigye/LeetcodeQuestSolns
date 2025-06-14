def mask_excess_characters(text, limit):
    """
    Returns a new string where characters appearing more than `limit` times are replaced with 'x'.
    Maintains the original order of characters.

    Args:
        text (str): The input string.
        limit (int): The maximum number of allowed occurrences for each character.

    Returns:
        str: A modified string where any character that appears more than `limit` times
             is replaced with 'x' after the limit is reached.

    Example:
        >>> mask_excess_characters("aabbcc", 1)
        'axbxcx'

        >>> mask_excess_characters("abcde", 1)
        'abcde'

        >>> mask_excess_characters("aaaabbccddddeeef", 2)
        'aaxxbbccddxxeexf'

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if len(text) == 0 or limit == 0:
        return ""
    
    result = ""
    count = {}

    for value in text:
        if value in count:
            count[value] += 1
        else:
            count[value] = 1

        if count[value] <= limit:
            result+=value
        else:
            result+='x'
    
    return result





# does not keep other of elements in text
# time complexity = 0(n), space complexity = 0(n)
from collections import Counter
def detect_excess(text, limit):
    if len(text) == 0 or limit == 0:
        return text
    
    result = ""
    character_dict = Counter(text)

    for char, freq in character_dict.items():
        if freq > limit:
            result+=char * (freq - limit)
        else:
            continue
    return result



# If you want the result to appear in order of original text
def detect_excess_in_order(text, limit):
    if not text or limit == 0:
        return text

    count = Counter(text)
    used = {}
    result = ""

    for char in text:
        used[char] = used.get(char, 0) + 1
        if used[char] > limit:
            result += char
    
    return result


user_input = input()
text, limit = user_input.strip().split()

# print(mask_excess_characters(text, int(limit)))
# print(detect_excess(text,int(limit)))

