# Practice Question 4: The Digital Receipt
# Objective: Combine input(), multiple arithmetic operations, and advanced f-string formatting. File: assignment4.py
# Instructions: Build a point-of-sale system for a local kiosk.
# 1.	Ask the user for the name of an item, the price (int), and the quantity bought (int).
# 2.	Calculate the subtotal.
# 3.	Calculate a discount of 5% on the subtotal (if subtotal is 1000, discount is 50). Hint: multiply by 0.05.
# 4.	Calculate the vat (16%) on the discounted amount (subtotal - discount).
# 5.	Calculate the total to be paid.
# 6.	Print a formatted receipt using f-strings. Format all money values to 2 decimal places and include commas (e.g., Ksh 1,200.00).
# 7.	Use an empty print() to create a blank line between the item details and the final total.

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
