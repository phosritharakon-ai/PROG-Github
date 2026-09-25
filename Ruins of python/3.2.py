power = int(input("Enter power: "))
key_color = input("Enter key color: ")

if power >= 50:
    if key_color == "gold":
        print("TREASURE")
    else:
        print("NEED KEY")
else:
    print("LOCKED")