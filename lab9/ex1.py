order = str(input("What do you want to eat: "))
price = float(input("Enter the price: "))
quantity = int(input(f"How many {order} do you want: "))

txt = "Result"
print(f"{txt:=^30}")

print(f"{'Item':<10} : {order}")
print(f"{'Price':<10} : {price:.2f} {'Bath':>6}")
print(f"{'Quantity':<10} : {quantity}")

print("-"*30)

subtotal = float(price*quantity)
vat = float(subtotal*0.07)
total = float(subtotal + vat)

print(f"{'Subtotal':<10} : {subtotal:.2f} {'Bath':>5}")
print(f"{'VAT 7%':<10} : {vat:.2f} {'Bath':>5}")
print(f"{'Total':<10} : {total:.2f} {'Bath':>5}")

print("="*30)