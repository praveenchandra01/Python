def esum(x):
    esum=0
    for i in x:
        if i%2==0:
            esum+=i
    return esum
def osum(x):
    osum=0
    for i in x:
        if i%2!=0:
            osum+=i
    return osum        
l=[eval(e) for e in input("Enter elements in list :").split(',')]
r=esum(l)
s=osum(l)
print("Even sum :",r,"Odd sum :",s)
input()
