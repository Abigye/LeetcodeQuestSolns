# calculate the sum of elements between two indices i and j (inclusive) multiple times. 

# brute force approach
def calculate_sum(nums, i, j):
    return sum(nums[i:j+1])

print(calculate_sum([1,2,3,4,5], 1, 3)) 
# time complexity is O(j - i + 1)


def calculate_sum_prefix_sum(nums, i, j):
    prefix_sum = []
    curr_sum = 0
    for index in range(i, j+1):
        curr_sum += nums[index]
        prefix_sum.append(curr_sum)
    return prefix_sum

print(calculate_sum_prefix_sum([1,2,3,4,5], 1, 3)) 
       

def prefix_sum_array(nums):
    n = len(nums)
    prefix_sum = [0] * n
    prefix_sum[0] = nums[0]


    for index in range(1, n):
        prefix_sum[index] = prefix_sum[index-1] + nums[index]

    return prefix_sum

print(prefix_sum_array([1,2,3,4,5]))
# time complexity is O(n)


#find the prefix sum of an array
# prefix sum is a technique that is used to find the sum of all the elements in a subarray
def prefix_sum(nums):
    n= len(nums)
    prefix_sum = [0] * n
    prefix_sum[0] = nums[0]

    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i-1] + nums[i]

    return prefix_sum

print(prefix_sum([1,2,3,4,5]))