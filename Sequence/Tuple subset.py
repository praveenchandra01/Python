t1=eval(input("Enter elements in tuple 1 :"))
t2=eval(input("Enter elements in tuple 2 :"))
r=set(t2).issubset(t1)
if r==True:
    print("Tuple t2 is subset of t1")
else:
    print("Not a subset")
input()
