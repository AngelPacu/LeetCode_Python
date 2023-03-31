# nums = [2,7,11,15]
# nums = [3,2,4]
# nums = [3,3]
# target = 6
# target = 9
# target = 6

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



