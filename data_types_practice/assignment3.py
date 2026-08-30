# Practice Question 3: The Chama (Savings Group) Calculator
# Objective: Use input(), arithmetic operators (/, //, %), and math functions. File: assignment3.py
# Instructions: You are building a tool for a local savings group (Chama).
# 1.	Ask the user to input the total amount of money contributed today (convert to int).
# 2.	Ask the user how many members are present today (convert to int).
# 3.	Calculate the exact share each member gets using normal division (/). Print it rounded to 2 decimal places.
# 4.	Calculate how many whole 100 Ksh notes each member gets using floor division (//).
# 5.	Calculate the loose change (remainder in Ksh) that cannot be divided evenly into 100 Ksh notes using modulus (%). Print this remainder.
# 6.	Use the max() function to find out the highest denomination if someone contributes an extra 500 Ksh, compared to the remainder.
#  (Hint: max(remainder, 500)).

total = int(input("Enter total amount contributed : "))
member_count = int(input("How many members are present today : "))

member_share = total / member_count
print(f"Each member split : {member_share}")

notes_count = member_share // 100
print(f"Each member gets : {notes_count} Ksh 100 notes")

loose_change = round(member_share % 100, 2)
print(f"Remainder amount: {loose_change}")

high_denom = max(loose_change, 500)
print(f"{high_denom}")
