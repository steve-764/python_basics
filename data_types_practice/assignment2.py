# Practice Question 2: The Type Detective

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
