# Practice Question 2: The Type Detective
# Objective: Master data types, understand the difference between strings and integers, and practice type casting. File: assignment2.py
# Instructions:
# 1.	Create a variable str_number and assign the string "50" to it.
# 2.	Create a variable int_number and assign the integer 50 to it.
# 3.	Print str_number + str_number and write a comment explaining why the output is 5050 instead of 100.
# 4.	Convert str_number into an integer, add 10 to it, and print the result.
# 5.	Ask the user to input their exact height in metres (e.g., 1.75) using input().
# 6.	Convert their input into a float, multiply it by 100 to get centimetres, 
#       and print it using an f-string: "You are {height_cm} cm tall."

str_number = "50"
int_number = 50
print(str_number + str_number)
# Will output 5050 since we are combining a string with an integer, 
# thus python performs a concatenation rather than an arithmetic operation.

str_number = int(str_number) + 10
print(str_number)

height = input("Enter your height in metres : ")
height_cm = float(height) * 100
print(f"You are {height_cm} cm tall.")
