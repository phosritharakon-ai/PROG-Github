length = float(input())
material = input()

is_valid = (length < 2.5) and (material in ["bronze", "copper", "silver"])
print(is_valid)