raw_input = input().split()

rows = int(raw_input[0])
cols = int(raw_input[1])
target = int(raw_input[2])

vulnerable_count = 0
max_vulnerable = 0

for i in range(rows):
    row_str = input().split()

    row_total = 0 #เริ่มนับที่ 0 ใหม่
    for item in row_str:
        num = int(item)
        row_total += num

    if row_total >= target: #เช็คว่าผ่านเกณฑ์มั้ย
        vulnerable_count += 1
        if row_total > max_vulnerable: #หาค่าผลรวมที่มากที่สุด
            max_vulnerable = row_total

print(vulnerable_count)
print(max_vulnerable)