item = int(input("How many item?: "))
money = int(input("How much?: "))

if item > 5:
    if money >= 500:
        print("Discount")
    else:
        print("No Discount")
else:
    print("Normal")