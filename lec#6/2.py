# a = [2, 4, 9]
# b = [10, 20, 30]
# c = [1, 5, 9, 13]

# print(sum(a) / len(a))
# print(sum(b) / len(b))
# print(sum(c) / len(c))

numbers = [[2, 4, 9],
            [10, 20, 30],
            [1, 5, 9, 13]]

for nums in numbers:
    avg = sum(nums) / len(nums)
    print(avg)
