class BalanceException(Exception):
  pass


class BankAccount : 
  def __init__(self , initalAmount , actName ) :
    self.balance = initalAmount
    self.name = actName
    print("---------------------------Create Account------------------------")
    print(f"\nAccount {self.name} created.\nBalance = {self.balance:.2f}$")
    print("---------------------------Create Account------------------------")

  def getBalance(self):
    print(f"\nAccount {self.name} balance is : {self.balance:.2f}$")




  def deposit(self , amount):
      self.balance += amount
      print("----------------------------Deposit------------------------------------")
      print(f"\nAccount {self.name} add deposit {amount}$ ")
      self.getBalance()
      print("----------------------------Deposit------------------------------------")
    


  def checkTransaction(self , withdraw):
    if self.balance >= withdraw :
      return
    else :
      raise BalanceException(f"Your account balance is insufficient.\nyou have {self.balance}\nYou need {(withdraw - self.balance):.2f}$")

  
  def withdraw(self , withdraw):
    try :
        self.checkTransaction(withdraw)
        self.balance -= withdraw
        print("---------------------------Withdraw----------------------------")
        print(f"Account {self.name} withdraw {withdraw}$")
        self.getBalance()
        print("---------------------------Withdraw---------------------------- ")
    except BalanceException as  error :
        print(f"\nWithdraw is intrrupted : {error} ")
   
        
  def transfer(self , amount , accName):
      try :
        print("-------------------------Transfer------------")
        self.checkTransaction(amount)
        self.withdraw(amount)
        accName.deposit(amount)
      
        print("\n****************\nTransfer Completed\n****************")
        print("-------------------------Transfer------------")

      except BalanceException as error :
        print(f"\nTransferded is intrrupted : {error} ")



class IntrestRewardAccount(BankAccount):
      def deposit(self, amount):
          self.balance += (amount * 1.05)
          print(f"\nDeposit Completetd")
          self.getBalance() 


class SavingAccount(IntrestRewardAccount):
      def __init__(self , initalAmount , actName):
          super().__init__(initalAmount , actName)
          self.fee = 5

      def transfer(self, amount, accName):
          try :
            print("\n****************\nTransfer Completed\n****************")
            self.checkTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            self.withdraw(amount + self.fee)
            accName.deposit(amount)
            print("\n****************\nTransfer Completed\n****************")
          except BalanceException as error :
            print(f"\nTransferded is intrrupted : {error} ")


      