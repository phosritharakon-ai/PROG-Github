n = int(input())
data = input().split()

sum = 0
count = 0

for item in range(n):
    num = int(data[item])
    sum += num

    if num % 2 == 0:
        count += 1

print(f"Sum : {sum}")
print(f"Count : {count}")