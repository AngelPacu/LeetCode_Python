# nums = [2,7,11,15]
# nums = [3,2,4]
# nums = [3,3]
# target = 6
# target = 9
# target = 6
#
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

nums = [2,7,11,15]
target = 9
final = []
for pos, i in enumerate(nums,1):
    for pos2, j in enumerate(nums[pos:], pos + 1):
        total = i + j
        if total == target:
            final = [pos-1, pos2-1]
            print(final)
            break



### EXAMPLES

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Input: nums = [3,3], target = 6
# Output: [0,1]