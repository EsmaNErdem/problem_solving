def longestFall(nums):
    if not nums: return 0
    max_count = 1
    # for first element, because p starts from 1
    count = 1
    for p in range(1, len(nums)):
        if nums[p - 1] > nums[p]:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 1

    return max_count

print(longestFall([5, 3, 1, 3, 0]))  # 3, 5-3-1 is the longest consecutive sequence of decreasing integers
print(longestFall([2, 2, 1]))  # 2, 2-1 is the longest consecutive sequence of decreasing integers
print(longestFall([2, 2, 2]))  # 1, 2 is the longest consecutive sequence of decreasing integers
print(longestFall([5, 4, 4, 4, 3, 2]))  # 3, 4-3-2 is the longest
print(longestFall([9, 8, 7, 6, 5, 6, 4, 2, 1]))  # 5, 9-8-7-6-5 is the longest
print(longestFall([]))  # 0
