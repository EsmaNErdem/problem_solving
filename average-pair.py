def averagePair(lst, target):
    if len(lst) == 0: return False

    l = 0
    r = len(lst) - 1
    while r > l:
        average =  (lst[l] + lst[r]) / 2
        if average == target: 
            return True
        elif average > target:
            r -= 1
        else:
            l += 1

    return False



print(averagePair([1, 2, 3], 2.5))  # True
print(averagePair([1, 3, 3, 5, 6, 7, 10, 12, 19], 8))  # True
print(averagePair([-1, 0, 3, 4, 5, 6], 4.1))  # False
print(averagePair([], 4))  # False