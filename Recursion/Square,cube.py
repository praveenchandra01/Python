def PrintN_Square(n):
    if n!=0:
        PrintN_Square(n-1)
        print(n*n,end=" ")
def PrintRev_Square(n):
    if n!=0:
        print(n*n,end=" ")
        PrintRev_Square(n-1)
def PrintN_Cube(n):
    if n!=0:
        PrintN_Cube(n-1)
        print(n**3,end=" ")
def PrintRev_Cube(n):
    if n!=0:
        print(n**3,end=" ")
        PrintRev_Cube(n-1)
        
n=int(input())
PrintN_Square(n)
print("...Square Series")
PrintRev_Square(n)
print("...Square Series in Reverse order")
PrintN_Cube(n)
print("...Cube Series")
PrintRev_Cube(n)
print("...Cube Series in Reverse order")
input()
