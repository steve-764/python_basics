# Practice Question 1: The Print & Variable Warm-up
# Objective: Practice using print(), creating variables, updating them, and using basic f-strings. File: assignment1.py
# Instructions:
# 1.	Create variables for a student: name (string), course (string), modules_completed (int), and is_active (bool).
# 2.	Print a greeting using an f-string: "Hello, {name}! Welcome to {course}."
# 3.	Update the modules_completed variable by adding 1 to it (simulating finishing a module today).
# 4.	Print the updated number of modules using an f-string: "You have now completed {modules_completed} modules."
# 5.	Print the data type of the is_active variable using the type() function.

name = "John Doe"
course = "python basics"
modules_completed = 0
is_active = True

print(f"Hello, {name}! Welcome to {course}")
modules_completed += 1
print(f"You have now completed {modules_completed} modules.")
print(type(is_active))
