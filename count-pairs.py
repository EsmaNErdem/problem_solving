def countPairs(nums, target):
    seen  = set()
    count = 0
    for n in nums:
        complement = target - n
        if complement in seen:
            count += 1

        seen.add(n)

    return count


# def countPairs(nums, target):
#     seen  = set()
#     res = []
#     for n in nums:
#         complement = target - n
#         if complement in seen:
#             res.append((n, complement))

#         seen.add(n)

#     return res

print(countPairs([3, 1, 5, 4, 2], 6))  # 2 (1, 5) and (2, 4)
print(countPairs([10, 4, 8, 2, 6, 0], 10))  # 3 (2, 8), (4, 6), and (10, 0)
print(countPairs([4, 6, 2, 7], 10))  # 1 (4, 6)
print(countPairs([1, 2, 3, 4, 5], 10))  # 0
print(countPairs([1, 2, 3, 4, 5], -3))  # 0
print(countPairs([0, -4], -4))  # 1 (0, -4)
print(countPairs([1, 2, 3, 0, -1, -2], 0))  # 2 (1, -1) and (2, -2)


