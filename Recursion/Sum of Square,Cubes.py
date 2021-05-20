def Sum_Sq(n):
    if n==1:
        return 1
    else:
        return n**2 + Sum_Sq(n-1)
def Sum_Cu(n):
    if n==1:
        return 1
    else:
        return n**3 + Sum_Cu(n-1)    
n=int(input("Enter the Limit :"))
r=Sum_Sq(n)
q=Sum_Cu(n)
print("Sum of Squares is :",r)
print("Sum of Cubes is :",q)            
