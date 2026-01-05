
class Bank:

    acc_num:int

    name:str

    acc_type =str

    balance =float

    def set_bankdetails(self,acc_num,name,acc_type,balance):

        self.acc_num=acc_num
        self.name=name
        self.acc_type=acc_type
        self.balance=balance

    def deposit(self,amount):

       self.balance+=amount

       print(f"your account{self.acc_num} credited with {amount} your avl is {self.balance}")

    def withdraw(self,amount):

        if amount<self.balance:

            self.balance-=amount

            print(f"your account {self.acc_num} debited  with {amount}your avl bal is {self.balance}")

        else:

            print("trasaction faild insufficient balance")

    def balance_enq(self):

        print(f"hai {self.name} your acc balance is {self.balance}")

bank_acccount1 =Bank()

bank_acccount1.set_bankdetails(90482234,"rishi","savings",20000)

bank_acccount1.withdraw(2000)

bank_acccount1.deposit(1000)


