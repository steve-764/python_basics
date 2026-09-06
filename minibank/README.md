# Mini Bank Menu Program

Build a Mini Bank menu program using `while True` and `break`:

```python
balance = 10000
```

Your program should:

Print a menu with these options:
- === Mini Bank ===

- Check balance
- Deposit
- Withdraw
- Exit


- Ask the user: `Choose option:`

- Use `if` / `elif` / `else` to handle each choice:
  - **Option 1** → Print the current balance
  - **Option 2** → Ask for a deposit amount, add it to balance, print the new balance
  - **Option 3** → Ask for a withdrawal amount:
    - If it's more than the balance, print "Insufficient funds!"
    - Otherwise subtract it from balance and print the new balance
  - **Option 4** → Print "Thank you. Goodbye!" and stop the program
  - **Anything else** → Print "Invalid option. Try again."

The menu should keep showing again and again until the user chooses option 4.