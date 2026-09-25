import copy

data = [[80, 75],
        [60, 85]]

dcopy = copy.deepcopy(data)
dcopy[1][0] = 1
print(dcopy)