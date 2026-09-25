hammer = float(input("The weight of hammer: "))
sword = float(input("The weight of sword: "))
shield = float(input("The weight of shield: "))

is_valid = (hammer <= sword + shield)
print(is_valid)