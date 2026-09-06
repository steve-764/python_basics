#                   Session 4 - Functions: Questions
# ======================================================

# Q1. Write a function called greet that prints 'Habari! Welcome to Python class.' Then call it.


def greet ():
    print("Habari! Welcome to Python class.")

greet()

# ======================================================

# Q2. Write a function called show_line that prints a line of 30 dashes. Call it three times in a row.

def show_line():
    print("-" * 30)

show_line()
show_line()
show_line()

# ======================================================

# Q3. Write a function called mpesa_menu that prints a simple M-Pesa menu (Send Money, Withdraw, Check Balance, Exit). Call it once.

def mpesa_menu ():
    print("Send Money")
    print("Withdraw")
    print("Check Balance")
    print("Exit")

mpesa_menu()

# ======================================================

# Q4. Write a function called greet_student that takes a name parameter and prints 'Habari, [name]! Ready to code?'

def greet_student(name):
    name = input("Enter your name : ")
    print(f"Habari, {name}! Ready to code?")

greet_student("name")

# ======================================================

# Q5. Write a function called print_times_table that takes a number parameter and prints its times table from 1 to 10.

def print_times_table (num):
    num = int(input("Enter a number : "))
    for i in range(1, 11):
        print(f"{num} X {i} = {num * i}")

print_times_table("num")

# ======================================================

# Q6. Write a function called add_mpesa that takes two parameters (sender and amount) and prints a transfer message.
#  E.g. 'Amina sent Ksh 500 via M-Pesa.'

def add_mpesa(sender, amount):
    sender = input("Enter sender name : ")
    amount = int(input("Enter amount : "))
    print(f"{sender} sent Ksh {amount} via M-Pesa.")

add_mpesa("sender", "amount")

# ======================================================

# Q7. Write a function called add that takes two numbers and returns their sum. Store the result in a variable and print it.

def add (num1, num2):
    num1 = int(input("Enter number 1 : "))
    num2 = int(input("Enter number 2 : "))
    print(f"{num1} + {num2} = {num1 + num2}")

add("num1", "num2")


# ======================================================

# Q8. Write a function called vat_price that takes an original price and returns the price after adding 16% VAT (Kenya's standard VAT rate).

def vat_price (price):
    price = int(input("Enter price : "))
    vat = price * 0.16
    print(f"The price after VAT (16%) is : {price + vat}")

vat_price("price")

# ======================================================

# Q9. Write a function called is_pass that takes a score and returns True if the score is 50 or above, and False otherwise.
#  Test it with several scores.

def is_pass (score):
    score = int(input("Enter the score : "))
    if score >= 50:
        output = "True"
    else:
        output = "False"
    print(f"{output}")

is_pass("score")

# ======================================================

# Q10. Write a function called average that takes a list of numbers and returns the average. Test it with exam scores.

def average ():
    count = 0
    total = 0
    print("Enter (0) to get average of values entered: ")

    while True:
        number = int(input("Enter number: "))
    
        if number == 0:
            break
        else:
            count += 1
            total += number
            avg = total / count
    print(f"The average is : {avg}")

average()

# ======================================================

# Q11. Write a function called make_tea that takes cups and an optional sugar parameter (default 1). 
# Print a message like 'Making 2 cups of tea with 1 spoon of sugar.'

def make_tea(cups, sugar = 1):
    cups = int(input("How many cups of tea will be made ? "))
    sugar = int(input("How many cubes of sugar to be added ? "))
    print(f"Making {cups} cups of tea with {sugar} spoon(s) of sugar.")

make_tea("cups", "sugar")


# ======================================================

# Q12. Write a function called send_message that takes recipient, message, and an optional channel parameter (default 'SMS'). 
# Print: 'Sending to [recipient] via [channel]: [message]'

def send_message(recipient, message, channel = "SMS"):
    recipient = input("who is receiving this message ? ")
    channel = input("what channel is the message going through ? ")
    message = input("Enter your message : ")
    print(f"Sending {recipient} via {channel} : {message}")


send_message("recipient", "message", "channel")

# ======================================================

# Q13. Receipt Generator: Write a program that uses functions to calculate and print a shop receipt. 
# Use separate functions for: calculating the subtotal, applying a discount, adding VAT, and printing the receipt.


def calculate_subtotal(prices):
    return sum(prices)


def apply_discount(subtotal):
    discount = subtotal * 0.10
    return subtotal - discount


def add_vat(amount):
    vat = amount * 0.16
    return amount + vat


def print_receipt(prices):
    subtotal = calculate_subtotal(prices)
    discounted_amount = apply_discount(subtotal)
    total = add_vat(discounted_amount)

    print("===== SHOP RECEIPT =====")
    print(f"Subtotal        : KES {subtotal}")
    print(f"Discount (10%)  : KES {subtotal * 0.10}")
    print(f"After Discount  : KES {discounted_amount}")
    print(f"VAT (16%)       : KES {discounted_amount * 0.16}")
    print(f"Total           : KES {total}")
    print("=" * 30)


# Ask the user for the number of items
number_of_items = int(input("How many items did you buy? "))

prices = []

# Collect the price of each item
for i in range(number_of_items):
    price = float(input(f"Enter the price of item {i + 1}: "))
    prices.append(price)

# Print the receipt
print_receipt(prices)


# ======================================================

# Q14. Student Grade Calculator: Write a program using functions that takes a student's name and three subject scores,
#  calculates their average, assigns a grade (A ≥ 70, B ≥ 60, C ≥ 50, D ≥ 40, F below 40), and prints a report. 
# Use a separate function for each task.

def get_student_name():
    return input("Enter student's name: ")

def get_scores():
    score1 = float(input("Enter score for Subject 1 : "))
    score2 = float(input("Enter score for Subject 2 : "))
    score3 = float(input("Enter score for Subject 3 : "))

    return score1, score2, score3


def calculate_average(score1, score2, score3):
    return (score1 + score2 + score3) / 3

def assign_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def print_report(name, score1, score2, score3, average, grade):
    print("===== STUDENT REPORT =====")
    print(f"Student Name : {name}")
    print(f"Subject 1    : {score1}")
    print(f"Subject 2    : {score2}")
    print(f"Subject 3    : {score3}")
    print(f"Average      : {round(average, 2)}")
    print(f"Grade        : {grade}")
    print("=" * 30)


# Get student information
name = get_student_name()

score1, score2, score3 = get_scores()

# Calculate average
average = calculate_average(score1, score2, score3)

# Assign grade
grade = assign_grade(average)

# Print report
print_report(name, score1, score2, score3, average, grade)