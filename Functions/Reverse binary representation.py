def bin_rev(x):
    b=bin(a)
    y=b[2::]
    z=y[len(y)::-1]
    print(y)
    print("REverse :",z)
    
a=int(input("Enter a number :"))
bin_rev(a)
input()
