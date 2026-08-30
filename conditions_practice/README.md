# Python Session 2 – Practice Questions

## QUESTION 1: Age Group Classifier

**Write a program that:**

- Asks the user for their age (convert to `int`).
- Classifies them into:
  - **Child** (`0–12`)
  - **Teenager** (`13–19`)
  - **Adult** (`20–64`)
  - **Senior** (`65+`)
- Prints: `"You are a [category]."`

---

## QUESTION 2: Even or Odd Checker

**Write a program that:**

- Asks the user for a number (convert to `int`).
- Checks if the number is even or odd.
- Prints:
  - `"[number] is an even number"`
  - or `"[number] is an odd number"`
- **Hint:** Use the modulo operator `%`.

  `number % 2 == 0` means the number is even.

---

## QUESTION 3: Pass/Fail with Subject Details

**Write a program that:**

- Asks for 3 subject scores:
  - Math
  - English
  - Science
- Calculates the average.
- If average `>= 50`, prints `"PASS"`.
- If average `< 50`, prints `"FAIL"`.
- Also prints the highest score among the 3 subjects.

---

## QUESTION 4: Discount Calculator

**Write a program that:**

- Asks for the total purchase amount (convert to `int`).
- Asks if the user is a member (`yes/no`).
- If member **AND** amount `>= 1000`: apply a **20% discount**.
- If member **AND** amount `< 1000`: apply a **10% discount**.
- If not a member **AND** amount `>= 1000`: apply a **5% discount**.
- If not a member **AND** amount `< 1000`: apply **no discount**.
- Prints the final amount payable with **2 decimal places**.

---

## QUESTION 5: Temperature Advice

**Write a program that:**

- Asks for today's temperature in Celsius (convert to `int`).
- Asks if it's raining (`yes/no`).
- Gives advice:
  - If temperature `> 30`: `"It's hot! Wear light clothes."`
  - If temperature is between `20–30` **AND** raining: `"Carry an umbrella."`
  - If temperature is between `20–30` **AND** not raining: `"Perfect weather!"`
  - If temperature `< 20`: `"It's cold. Wear a jacket."`

---

## QUESTION 6: Voting Eligibility

**Write a program that:**

- Asks for age (convert to `int`).
- Asks for citizenship (`Kenyan/Other`).
- A person can vote if they are `18+` **AND** Kenyan.
- Prints:
  - `"You are eligible to vote"`
  - or `"You are not eligible to vote"`
- If not eligible, explain why:
  - Age issue
  - Citizenship issue
  - Or both

---

## QUESTION 7: Loan Approval System

**Write a program that:**

- Asks for monthly salary (convert to `int`).
- Asks for credit score (convert to `int`).
- If salary `>= 30000` **AND** credit score `>= 700`:
  - `"Loan Approved"`
- If salary `>= 30000` **AND** credit score is between `600–699`:
  - `"Loan Approved with higher interest"`
- If salary `< 30000` **OR** credit score `< 600`:
  - `"Loan Denied"`
- Prints the result with the specific reason.

---

## QUESTION 8: Fuel Level Warning

**Write a program that:**

- Asks for the fuel level in litres (convert to `int`).
- If fuel `< 10`:
  - `"LOW FUEL! Please refuel immediately."`
- If fuel is between `10–25`:
  - `"Fuel is running low. Plan to refuel soon."`
- If fuel `> 25`:
  - `"Fuel level is good."`
- If fuel `> 50`:
  - `"Fuel tank is full. You're good to go!"`

> **Note:** Think carefully about the order of your `if`/`elif` conditions because values above 50 also satisfy `fuel > 25`.

---

## QUESTION 9: Matatu Fare Calculator (with Passenger Type)

**Write a program that:**

- Asks for distance in km (convert to `int`).
- Asks if the passenger is a student (`yes/no`).
- Determines the base fare:
  - `0–5 km`: **Ksh 50**
  - `6–15 km`: **Ksh 80**
  - `16–30 km`: **Ksh 120**
  - Above `30 km`: **Ksh 180**
- Students get a **20% discount**.
- Prints the final fare with the discount applied if applicable.

---

## QUESTION 10: Password Strength Checker

**Write a program that:**

- Asks the user to create a password.
- Checks password strength:
  - If length `>= 8` **AND** contains a number:
    - `"STRONG password"`
  - If length `>= 8` but has no number:
    - `"MEDIUM password - add numbers"`
  - If length `< 8`:
    - `"WEAK password - must be at least 8 characters"`
- **Hint:** Use `.isdigit()` to check for numbers in a string.

---

## QUESTION 11: M-Pesa Transaction Fee Calculator

**Write a program that:**

- Asks for the amount to send (convert to `int`).
- Calculates the transaction fee:
  - Amount `<= 100`: **Fee = 0**
  - Amount `101–500`: **Fee = 7**
  - Amount `501–1000`: **Fee = 12**
  - Amount `1001–1500`: **Fee = 18**
  - Amount `> 1500`: **Fee = 25**
- Asks if the user has a **Bonga Points discount** (`yes/no`).
- If yes, apply **50% off the fee**.
- Prints:

`"Amount: Ksh X | Fee: Ksh Y | Total: Ksh Z"`

---

## QUESTION 12: Restaurant Order System

**Write a program that:**

- Asks for the type of meal (`breakfast/lunch/dinner`).
- For breakfast, display:
  - `"Breakfast menu: Mandazi, Chapati, Tea"`
- For lunch, display:
  - `"Lunch menu: Ugali, Rice, Beef, Vegetables"`
- For dinner, display:
  - `"Dinner menu: Pilau, Chicken, Salad"`
- Asks if the user wants a drink (`yes/no`).
- If yes, suggests a drink based on the meal type:
  - Breakfast: `"Try our Chai!"`
  - Lunch: `"Try our Fresh Juice!"`
  - Dinner: `"Try our Maziwa Lala!"`

---

## QUESTION 13: Grade Comment System

**Write a program that:**

- Asks for the student's name.
- Asks for the score (`0–100`).
- Assigns a grade and provides a comment:

| Grade | Score | Comment |
|---|---:|---|
| A | 80–100 | `"Excellent performance! Keep it up!"` |
| B | 70–79 | `"Good job! You're doing well."` |
| C | 60–69 | `"Satisfactory. Room for improvement."` |
| D | 50–59 | `"Needs improvement. Work harder!"` |
| F | 0–49 | `"Poor performance. Must retake."` |

---

## QUESTION 14: Electricity Bill Calculator

**Write a program that:**

- Asks for units consumed (convert to `int`).
- Calculates the bill using the following rates:
  - First 50 units: **Ksh 10 per unit**
  - Next 50 units (`51–100`): **Ksh 15 per unit**
  - Next 100 units (`101–200`): **Ksh 20 per unit**
  - Above 200 units: **Ksh 25 per unit**
- If the total bill is `> 2000`, apply a **10% discount**.
- Prints a detailed breakdown and the total bill.

---

## QUESTION 15: Complete Student Report Card

**Write a program that:**

### Input

Ask for:

- Student name
- 4 subject scores:
  - Math
  - English
  - Science
  - History
- Attendance percentage

All scores and attendance should be converted to `int`.

### Calculate

#### 1. Total Score

Calculate the total score out of 400.

#### 2. Average Score

Calculate the average score.

#### 3. Grade

Assign a grade based on the average:

| Average | Grade | Description |
|---:|:---:|---|
| 80–100 | A | Distinction |
| 70–79 | B | Merit |
| 60–69 | C | Credit |
| 50–59 | D | Pass |
| Below 50 | F | Fail |

#### 4. Promotion Status

Determine promotion using the following rules:

- If average `>= 50` **AND** attendance `>= 75`:
  - `"PROMOTED"`
- If average `>= 50` **AND** attendance `< 75`:
  - `"CONDITIONAL - Improve attendance"`
- If average `< 50`:
  - `"REPEAT - Failed exams"`

#### 5. Highest Score

Find the highest score and the subject in which it was achieved.

### Output

Print a complete, formatted report card with separators.

The report card should include:

- Student name
- Math score
- English score
- Science score
- History score
- Total score
- Average score
- Grade
- Grade description
- Attendance
- Highest score and subject
- Promotion status