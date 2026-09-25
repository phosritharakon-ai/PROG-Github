weight = float(input("Enter your weight: "))
height_cm = float(input("Enter your height: "))

height_m = height_cm / 100 #แปลงเซนติเมตรเป็นเมตร
bmi = weight / (height_m**2)

print(f"{bmi:.2f}")