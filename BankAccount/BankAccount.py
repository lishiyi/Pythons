'''
In this project, we'll create a Python class that can be used to create and manipulate a personal bank account.

The bank account class you'll create should have methods for each of the following:

Accepting deposits
Allowing withdrawals
Showing the balance
Showing the details of the account'''

class BankAccount(object):
  balance = 0
  
  def __init__(self, name):
    self.name = name
  
  def __repr__(self):
    return "Your balance is %.2f" % (self.balance)
  
  def show_balance(self):
    print "Your balance is %.2f" % (self.balance)
  
  def deposit(self, amount):
    if amount < 0:
      print "The amount should be greater than 0."
      return
    else:
      print "Depositing %.2f ..." %(amount)
      self.balance += amount
      self.show_balance()
      
  def withdraw(self, amount):
    if amount < 0 or amount > self.balance:
      print "Invalid amount, please try again."
    else:
      print "Withdrawing %.2f ..." %(amount)
      self.balance -= amount
      self.show_balance()
 
my_account = BankAccount("Shiyi")
print my_account
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print my_account