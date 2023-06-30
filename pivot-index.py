def pivotIndex(nums):
    l, r = 0, sum(nums)

    for i, num in enumerate(nums):
        r -= num
        if r == l:
            return i
        l += num
    return -1


print(pivotIndex([1, 2, 1, 6, 3, 1]))  # 3
print(pivotIndex([5, 2, 7]))  # -1
print(pivotIndex([-1, 3, -3, 2]))  # 1


 