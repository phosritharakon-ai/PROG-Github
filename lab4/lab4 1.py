name = str(input("Name: "))
age = int(input("Age: "))
gpa = float(input("GPA: "))
is_enrolled = input("Are you enrolled(True or Fales): ")=="True"

print(f"Name: {name}{type(name)}")
print(f"Age: {age}{type(age)}")
print(f"GPA: {gpa:.2f}{type(gpa)}")
print(f"Enrolled: {is_enrolled}{type(is_enrolled)}")