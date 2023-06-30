def twoArrayObject(keys, values):
    res = {}
    for i in range(len(keys)):
        if i < len(values):
            res[keys[i]] = values[i]
        else:
            res[keys[i]] = None

    return res
        
print(twoArrayObject(['a', 'b', 'c', 'd'], [1, 2, 3]))  # {'a': 1, 'b': 2, 'c': 3, 'd': None}
print(twoArrayObject(['a', 'b', 'c'], [1, 2, 3, 4]))  # {'a': 1, 'b': 2, 'c': 3}
print(twoArrayObject(['x', 'y', 'z'], [1, 2]))  # {'x': 1, 'y': 2, 'z': None}