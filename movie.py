age_input = int(input("Enter your age: "))

if age_input < 0:
    print("Your age are invalid")
else:
    day_type = input("Enter weekday or weekend: ")
    
    if day_type not in ["weekday", "weekend"]:
        print("Please enter only weekday or weekend")
        exit()

    if age_input <= 12:
        print("Your type is child")
        if day_type == "weekday":
            print("Your cost is $6")
        else: print("Your cost is $8")
    elif 12 < age_input <= 64:
        print("Your type is adult")
        if day_type == "weekday":
            print("Your cost is $11")
        else: print("Your cost is $14")
    else:
        print("Your type is elder")
        if day_type == "weekday":
            print("Your cost is $8")
        else: print("Your cost is $10")
