n = int(input())

data = input().split()

first_num = int(data[0])
max = first_num
min = first_num

for i in range(n):
    num = int(data[i])
    if num > max:
        max = num
    if num < min:
        min = num

print(max)
print(min)