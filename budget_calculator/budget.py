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


