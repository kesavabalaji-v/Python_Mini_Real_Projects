# Bank Account: Encapsulation in Python

A small beginner example of **encapsulation**: keeping an object's data together with the methods that safely use it.

## Run the example

Open a terminal in this folder and run:

```bash
python bank_account.py
```
....
The example creates an account, deposits money, withdraws money, and displays the balance.

## How encapsulation is used

- `__balance` is kept inside the `BankAccount` object. The double underscore triggers Python's name-mangling, which discourages outside code from changing it directly. It is not strict security.
- `deposit()` and `withdraw()` are the controlled ways to change the balance. They reject non-positive amounts, and `withdraw()` also prevents spending more than the available balance.
- `get_balance()` returns the current balance, and `display_balance()` prints it for the user.

For example:

```python
account = BankAccount("Alex", 100)
account.deposit(25)
account.withdraw(10)
account.display_balance()  # Alex's balance: $115.00
```

## Put this project on GitHub

These commands assume Git is installed and you are signed in to GitHub through your usual Git setup. Create an empty repository on GitHub first, then replace `<your-repository-url>` below with the URL GitHub shows for that repository.

```bash
git init
git add bank_account.py README.md
git commit -m "Add Python encapsulation bank account example"
git branch -M main
git remote add origin <your-repository-url>
git push -u origin main
```

What each command does:

1. `git init` starts version control in this folder.
2. `git add ...` stages the two project files for saving.
3. `git commit ...` saves the staged files as a named snapshot.
4. `git branch -M main` names the current branch `main`.
5. `git remote add origin ...` connects this local project to your GitHub repository.
6. `git push -u origin main` uploads the branch to GitHub and remembers its remote branch for future pushes.
