raw_input = input().split()

rows = int(raw_input[0])
cols = int(raw_input[1])

count = 0
total = 0

for i in range(rows):
    row_str = input().split()
    for item in row_str:
        num = int(item)
        if 10 <= num <= 50 and num % 2 == 0:
            count += 1 #เก็บค่าที่ผ่านเกณฑ์
            total += num #ผลรวมของเลขที่ผ่านเกณฑ์

print(count)
print(total)