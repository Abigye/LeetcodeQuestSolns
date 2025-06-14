# getting the maximum subarray (of size 
# tc = 0(n), space = 0(k)
def maximum_k_subarray(nums,k):
    n = len(nums)

    if n < k:
        return 0
    
    curr_sum = 0
    sub_array = []

    # sub_array = nums[:k]  #0(k) space 0(k)
    # curr_sum = sum(sub_array)

    for i in range(k):
        curr_sum += nums[i]
        sub_array.append(nums[i])

    max_sum = curr_sum
    
    left = 0
    right = k

    best_sub_array = sub_array.copy()

    while right < n:
        curr_sum = curr_sum - nums[left] + nums[right]

        sub_array.pop(0)
        sub_array.append(nums[right])

        if curr_sum > max_sum:
            max_sum = curr_sum
            best_sub_array = sub_array.copy()

        left += 1
        right += 1

    return max_sum, best_sub_array


# print(maximum_k_subarray([1, 4, 2, 10, 23, 3, 1, 0, 20], 4))
# # Output: (39, [10, 23, 3, 3])

# print(maximum_k_subarray([5, 2, -1, 0, 3], 3))
# # Output: (6, [5, 2, -1])


def maximum_k_subarray_2(nums,k):
    n = len(nums)

    if n < k:
        return 0

    sub_array = nums[:k]  #0(k) space 0(k)
    curr_sum = sum(sub_array)
  
    left = 0
    right = k

    best_sub_array = sub_array.copy()
    max_sum = (curr_sum, best_sub_array)

    while right < n:
        curr_sum = curr_sum - nums[left] + nums[right]

        sub_array.pop(0)
        sub_array.append(nums[right])
        best_sub_array = sub_array.copy()

        max_sum = max(max_sum, (curr_sum,best_sub_array))

        left+=1
        right+=1

    return max_sum

print(maximum_k_subarray_2([1, 4, 2, 10, 23, 3, 1, 0, 20], 4))
# Output: (39, [10, 23, 3, 3])

print(maximum_k_subarray_2([5, 2, -1, 0, 3], 3))
# Output: (6, [5, 2, -1])



# def maximum_k_subarray_all(nums, k):
#     n = len(nums)

#     if n < k:
#         return 0

#     sub_array = nums[:k]  #0(k) space 0(k)
#     curr_sum = sum(sub_array)
  
#     left = 0
#     right = k

#     best_sub_array = sub_array.copy()
#     max_sum = (curr_sum, best_sub_array)

#     sub_arrays = []

#     while right < n:
#         curr_sum = curr_sum - nums[left] + nums[right]

#         sub_array.pop(0)
#         sub_array.append(nums[right])
#         best_sub_array = sub_array.copy()

#         max_sum = max(max_sum, (curr_sum,best_sub_array))
#         sub_arrays.append(max_sum)

#         left+=1
#         right+=1

#     return sub_arrays

# print(maximum_k_subarray_all([1, 4, 2, 10, 23, 3, 1, 3, 20], 4))
# # Output: (39, [10, 23, 3, 3])

# print(maximum_k_subarray_all([5, 2, -1, 0, 3], 3))
# # Output: (6, [5, 2, -1])