# Instructions
# •	Ask for the user's name and monthly salary (as an int).
# •	Ask for 4 monthly expenses by name and amount 
# - all as int: rent, food, transport, other.
# •	Calculate total_expenses = sum of all 4 expenses.
# •	Calculate savings = salary - total_expenses.
# •	Calculate savings_percent = (savings / salary) × 100.
# Print a full budget report using f-strings, showing:
# •	Name and salary
# •	Each expense on its own line
# •	Total expenses
# •	Savings amount
# •	Savings as a percentage, rounded to 1 decimal place


name = input("Enter your name : ")
salary = int(input("Enter your monthly salary : "))
print()
rent = int(input("How much do you spend on rent: "))
food = int(input("How much do you spend on food: "))
transport = int(input("How much do you spend on transport: "))
other = int(input("How much do you spend on other expenses: "))
print()
total_expenses = rent + food + transport + other
savings = salary - total_expenses
savings_percent = round((savings / salary) * 100, 1)


print("=" * 30)
print(f"{name} BUDGET REPORT")
print("=" * 30)
print(f"Salary : {salary}")
print("Your expenses are:")
print(f"Rent        : {rent}")
print(f"Food        : {food}")
print(f"Transport   : {transport}")
print(f"Other       : {other}")
print(f"Savings     : {savings} ({savings_percent} % of salary.)")


