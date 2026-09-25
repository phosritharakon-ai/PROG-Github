let = input("Enter letter: ")
row = int(input("How many line: "))

for i in range((row)+1):
    for j in range(i):
        print(f"{let}",end= "")
    print()