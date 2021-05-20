P=int(input("Enter principal amount :"))
r=float(input("Enter rate of intreast :"))
t=int(input("Enter time in years :"))
A=(P*pow(1+(r/100),t))
ci=A-P
print("Coumpound intreast is :",ci)        
