# Given an integer array nums sorted in non-decreasing order, 
# return an array of the squares of each number sorted in non-decreasing order.


# For example, if the input is [-4, -1, 0, 3, 10], the output should be [0, 1, 9, 16, 100].

def squares(nums):
    left = 0
    right = len(nums) - 1
    square = []
    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2
        if left_square > right_square:
            square.append(left_square)
            left+=1
        else:
            square.append(right_square)
            right-= 1
    square.reverse()
    return square

# time complexity = 0(n) though each append(0(1) amortized, reverse= 0(n)), space = 0(n)
print(squares([-4, -1, 0, 3, 10]))


def squares_inplace(nums):
    n = len(nums)
    result = [0] * n  # Preallocate result list
    left = 0
    right = n - 1
    pos = n - 1  # Start filling from the end

    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2

        if left_square > right_square:
            result[pos] = left_square
            left += 1
        else:
            result[pos] = right_square
            right -= 1

        pos -= 1
    
    return result
# time complexity = 0(n) though each append(0(1) amortized, space=0(n)
print(squares_inplace([-4, -1, 0, 3, 10]))
