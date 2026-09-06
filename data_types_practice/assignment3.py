# Practice Question 3: The Chama (Savings Group) Calculator

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
