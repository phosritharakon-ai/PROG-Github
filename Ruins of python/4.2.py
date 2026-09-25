n = int(input())

for i in range(1, n + 1): #บวก 1 เพราะเอา 4 ด้วย (แถว)
    for j in range(i): #จำนวนที่ต้องทำซ้ำ
        print(i, end=" ")
    print()