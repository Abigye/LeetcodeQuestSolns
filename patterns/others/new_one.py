from itertools import combinations
from typing import List
from collections import deque

'''
write a function that finds the set of all numbers from a list that adds up to a target number without repetition of the same number unless there are duplicates in the list
'''

def find_set(nums:List[int], target:int) -> List[int]:
    queue = deque()
    result = []
    queue.append(([], 0, 0)) # [current_set, current_sum, current_index]

    while queue:
        
        combination, current_sum, current_index = queue.popleft()

        if current_sum == target:
            result.append(combination)
            continue

        if current_sum > target:
            continue
        
        for i in range(current_index, len(nums)):
            # print(f"combination: {combination+[nums[i]]}, current_sum: {current_sum+nums[i]}, current_index: {current_index}, i: {i}")
            queue.append((combination + [nums[i]], current_sum + nums[i], i))
            # print(queue)

    return result

       
   
# print(find_set([1,2,3,4,5], 5))
# print(find_set([1, 2, 2, 3, 4, 5], 10))



# def valid_parenthesis(s:str) -> bool:
#     for i in range(len(s)):
#         for j in range(i+1, len(s)):
#             if s[i] == s[j]:
#                 return False
#     return True

# not efficient time complexity is O(2^n * k)   space complexity is O(2^n * n)
def generate_all_combos(nums, target):
    combos = [[]]
    result = []
    for num in nums:
        combos+=[[num]+ combo for combo in combos]

    for combo in combos:
        if sum(combo) == target:
            result.append(combo)
    return result

print(generate_all_combos([1,2,3,4], 5)) 


# attempt to use backtracking
def find_target_sum(nums, target):
    result = []

    def backtrack(start, curr_combo,curr_sum):
        if curr_sum == target:
            result.append(curr_combo)
            return

        if curr_sum > target:
            return # stop exploring
        
        for i in range(start, len(nums)):
            curr_combo.append(nums[i])
            backtrack(i, curr_combo, curr_sum + nums[i])
            curr_combo.pop()

    backtrack(0,[],0)
    return result



