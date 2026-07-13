# Q2. Bank Account
# Create a class BankAccount:

# attributes: account_holder, balance
# methods: deposit(amount), withdraw(amount)

# Withdraw only if balance is sufficient.
# Print final balance.


class BankAccount():
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self,amount):
        self.balance = self.balance + amount
        return f"Balance is updated current balance is: {self.balance}"
    
    def withdraw(self,wamount):
        if wamount <= self.balance:
            self.balance = self.balance - wamount
            return f" Current balance: {self.balance} and withdraw amount is {wamount}"
        else:
            return f"Required amount is less than availabe balance is: {self.balance}"

bankob = BankAccount("Majoj",1000)


while True:
    action = int(input("Enter 1 for withdraw and 2 for Deposit and 3 for exit"))
    if action == 1:
        withamout =  int(input("Please Enter the Amount You want to withdraw"))
        print(bankob.withdraw(withamout))
    elif action ==2:
        depositam = int(input("Please Enter the Amount You want to Deposit"))
        print(bankob.deposit(depositam))
    elif action == 3:
        exit()
    else:
        print("Please Enter the Valid input")




   









    



