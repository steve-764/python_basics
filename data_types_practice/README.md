# Python Practice Questions

## Practice Question 1: The Print & Variable Warm-up

**Objective:** Practice using `print()`, creating variables, updating them, and using basic f-strings.

**File:** `assignment1.py`

### Instructions

1. Create variables for a student:
   - `name` (string)
   - `course` (string)
   - `modules_completed` (int)
   - `is_active` (bool)

2. Print a greeting using an f-string:

   `"Hello, {name}! Welcome to {course}."`

3. Update the `modules_completed` variable by adding 1 to it (simulating finishing a module today).

4. Print the updated number of modules using an f-string:

   `"You have now completed {modules_completed} modules."`

5. Print the data type of the `is_active` variable using the `type()` function.

---

## Practice Question 2: The Type Detective

**Objective:** Master data types, understand the difference between strings and integers, and practice type casting.

**File:** `assignment2.py`

### Instructions

1. Create a variable `str_number` and assign the string `"50"` to it.

2. Create a variable `int_number` and assign the integer `50` to it.

3. Print `str_number + str_number` and write a comment explaining why the output is `5050` instead of `100`.

4. Convert `str_number` into an integer, add `10` to it, and print the result.

5. Ask the user to input their exact height in metres (e.g., `1.75`) using `input()`.

6. Convert their input into a float, multiply it by `100` to get centimetres, and print it using an f-string:

   `"You are {height_cm} cm tall."`

---

## Practice Question 3: The Chama (Savings Group) Calculator

**Objective:** Use `input()`, arithmetic operators (`/`, `//`, `%`), and math functions.

**File:** `assignment3.py`

### Instructions

You are building a tool for a local savings group (Chama).

1. Ask the user to input the total amount of money contributed today (convert to `int`).

2. Ask the user how many members are present today (convert to `int`).

3. Calculate the exact share each member gets using normal division (`/`). Print it rounded to 2 decimal places.

4. Calculate how many whole **100 Ksh** notes each member gets using floor division (`//`).

5. Calculate the loose change (remainder in Ksh) that cannot be divided evenly into 100 Ksh notes using modulus (`%`). Print this remainder.

6. Use the `max()` function to find out the highest denomination if someone contributes an extra **500 Ksh**, compared to the remainder.

   **Hint:** `max(remainder, 500)`

---

## Practice Question 4: The Digital Receipt

**Objective:** Combine `input()`, multiple arithmetic operations, and advanced f-string formatting.

**File:** `assignment4.py`

### Instructions

Build a point-of-sale system for a local kiosk.

1. Ask the user for:
   - The name of an item
   - The price (int)
   - The quantity bought (int)

2. Calculate the **subtotal**.

3. Calculate a **discount** of 5% on the subtotal.

   If the subtotal is 1000, the discount is 50.

   **Hint:** Multiply by `0.05`.

4. Calculate the **VAT** (16%) on the *discounted amount*:

   `subtotal - discount`

5. Calculate the **total** to be paid.

6. Print a formatted receipt using f-strings. Format all money values to 2 decimal places and include commas.

   **Example:** `Ksh 1,200.00`

7. Use an empty `print()` to create a blank line between the item details and the final total.

### Example Output

```text
================================
          DIGITAL RECEIPT
================================
Item: Bread
Price: Ksh 100.00
Quantity: 12
Subtotal: Ksh 1,200.00
Discount: Ksh 60.00
VAT: Ksh 182.40

Total: Ksh 1,322.40
================================