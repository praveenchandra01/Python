class insufficientbalance(ZeroDivisionError):
    def __init__(self,arg):
        self.msg=arg
balance=5000
w=int(input("Enter amount to withdraw"))
try:
    if w>balance:
        raise insufficientbalance ("Insufficient Balance in account")   
    balance=balance-w
except insufficientbalance as i:
    print("Execption",i.msg)
else:
    print("Withdraw amount",w,"Successfully")
finally:
    print("Current Balance is",balance)
input()
