# Practice Question 4: The Digital Receipt

name = input("Enter item name : ")
price= int(input("Enter item price : "))
quantity = int(input("Enter amount : "))
sub_total = price * quantity
discount = round(sub_total * 0.05, 2)
vat = round((sub_total - discount ) * 0.16, 2)
total = round(sub_total - discount - vat, 2)

print("=" * 30)
print("        KIOSK RECEIPT")
print("=" * 30)
print(f"Item        : {name}")
print(f"Quantity    : {quantity}")
print(f"Subtotal    : {sub_total}")
print(f"Discount    : {discount}")
print(f"VAT (16%)   : {vat}")
print()
print(f"Total       : KSH {total: ,}")
