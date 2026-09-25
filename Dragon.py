n = int(input("Dragon's Breath: "))
formula = 9000000000 * (1.05 ** n - 1) / 0.05

print(f"Total Cost: {int(formula)}")