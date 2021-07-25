class Account:
    rate_of_interest = 3.8  # static variable

    def __init__(self, a, b):
        self.AccountNum = a
        self.Balance = b
        # Account.rate_of_interest=3.8

    def Show_accno(self):
        print("Account num :", self.AccountNum)

    def Show_balance(self):
        print("\nBalance :", self.Balance)

    @staticmethod
    def Show_Rate_of_Interest():
        # Account.rate_of_interest=3.8
        print("\nRate of Interest :", Account.rate_of_interest)

    def withdraw(self):
        self.n = self.Balance
        self.w = int(input("\nEnter the Amount you want to withdraw :"))
        if self.w > self.Balance:
            print("Insufficient Balance")
        else:
            print("Current Balance :", self.Balance)
            self.n = self.Balance-self.w
            print("Withdraw amount", self.w, "Successfully")
            print("Balance after Withdraw :", self.n)

    def deposit(self):
        d = int(input("\nEnter the Amount you want to deposite :"))
        print("Current Balance", self.n)
        self.n += d
        print("Balance After Deposit :", self.n)

    def Simple_Int(self):
        #   p=input("Enter the principal amount: ")
        #   r=input("Enter the rate of intrest: ")
        t = int(input("\nEnter the time in years for Calculating Simple Interest : "))
        si = (self.Balance+Account.rate_of_interest+t)/100
        print("Simple intrest is: ", si)

    def Compound_int(self):
        t = int(input("\nEnter time in years for Calculating Compound Interest :"))
        A = (self.Balance*pow(1+(Account.rate_of_interest/100), t))
        ci = A-self.Balance
        print("Coumpound intreast is :", ci)


A1 = Account(1104201714, 5000)
A1.Show_accno()
A1.Show_balance()
Account.Show_Rate_of_Interest()
A1.Simple_Int()
A1.Compound_int()
A1.withdraw()
A1.deposite()
print("Thank You!")
input()
