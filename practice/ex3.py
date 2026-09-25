n = int(input())
data = input().split()
target = int(input())

count = 0

for i in range(n):
    num = int(data[i])

    if num == target:
        if count == 0:
            print("Found at index: ", end=" ")
        
        print(i, end=" ")
        count += 1

if count == 0:
    print("Not found")