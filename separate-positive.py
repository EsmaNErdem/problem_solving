def separatePositive(lst):
    l = 0
    r = len(lst) - 1

    while r > l:
        # keep moving left pointer until we find a negative num
        while lst[l] > 0 and l < len(lst) - 1:
            l += 1
        # keep moving right pointer until we find a positive num
        while lst[r] < 0 and r >= 0:
            r -= 1

        # once we finished either loop swap
            # for left pointer we hit the negative
            # for rigth we hit the positive
         
        lst[l], lst[r] = lst[r], lst[l]
        l += 1
        r -= 1

    return lst

print(separatePositive([2, -1, -3, 6, -8, 10]))  # [2, 10, 6, -3, -1, -8]
print(separatePositive([5, 10, -15, 20, 25]))  # [5, 10, 25, 20, -15]
print(separatePositive([-5, 5]))  # [5, -5]
print(separatePositive([1, 2, 3]))  # [1, 2, 3]