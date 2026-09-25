import random

grid = [] #สร้างลิสต์ว่างรอรับข้อมูล

for i in range(3): #Loop นอก สร้างทีละแถว 3 รอบ
    row = [] #ลิสต์รอรับเลขในแต่ละแถว

    for j in range(3): #ใส่เลข 3 ตัวในแถม (3 รอบ)
        num = random.randint(1, 100) #สุ่มเลข 1-100
        row.append(num) #เอาเลขใส่ใน row

    grid.append(row) #พอจบ loop ให้เอาทั้งแถวไปใส่ใน grid

print(grid) #แสดงผลลัพธ์