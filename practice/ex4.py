x = int(input())

data = input().split()

passed = 0
failed = 0

for i in range(x):
    num = int(data[i])
    if num >= 50:
        passed += 1
    if num < 50:
        failed += 1

print(f"Passed: {passed}")
print(f"Failed: {failed}")