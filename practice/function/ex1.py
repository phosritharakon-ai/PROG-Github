def calculate_tax(price, is_member):
    if is_member == "YES":
        tax = price * 0.05
    else:
        tax = price * 0.07
    
    return tax

input_price = int(input())
input_member = input().upper()

result_tax = calculate_tax(input_price, input_member)

print(f"Tax: {result_tax}")