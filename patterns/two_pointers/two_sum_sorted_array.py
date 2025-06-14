# Find two numbers that add up to a target using two pointers., Two Sum II - Input Array Is Sorted

# when aray is already sorted
def two_sum_2(nums, target):
    result = []
    left = 0
    right = len(nums) - 1

    while left < right:
        curr_sum = nums[left] + nums[right]
        if curr_sum == target:
            result.append((nums[left], nums[right]))
            left += 1
            right -= 1
        elif curr_sum > target:
            right -= 1
        else:
            left += 1
    return result

# print(two_sum_2([2, 7, 11, 15], 9)) #2,7
# print(two_sum_2([1, 1, 2, 3, 4], 2)) # 1,1
# print(two_sum_2([1, 2, 2, 3, 4], 4)) #2,2 , 1,3
# print(two_sum_2([-5, -2, 0, 3, 4], -7))   #-5,-2
# print(two_sum_2([1, 2, 3, 4, 10], 11)) # 1,10
# print(two_sum_2([1, 3, 4, 5, 6], 9)) # 3,6 , 4,5




# def two_sum_unsorted(nums, target):
#     nums.sort()
#     #  then follow the same steps for two sum unsorted

# for all cases
def two_sum(nums, target):
    result = []
    complements = {}

    for num in nums:
        complement = target - num
        if num in complements:
            result.append((num, complements[num]))
        else:
            complements[complement] = num
    
    return result
# time complexity = 0(n)

print(two_sum([-5, -2, 0, 3, 4], -7))   #-5,-2
print(two_sum([1, 2, 3, 4, 10], 11)) # 1,10
print(two_sum([1, 3, 4, 5, 6], 9)) # 3,6 , 4,5

def two_sum_index(nums, target):
    result = []
    complements = {}

    for i, num in enumerate(nums):
        complement = target - num
        if num in complements:
            result.append((i, complements[num]))
        else:
            complements[complement] = i
    
    return result
# time complexity = 0(n)

print(two_sum_index([-5, -2, 0, 3, 4], -7))   #-5,-2
print(two_sum_index([1, 2, 3, 4, 10], 11)) # 1,10
print(two_sum_index([1, 3, 4, 5, 6], 9)) # 3,6 , 4,5
print(two_sum_index([3,4,7,3,2], 6))              
