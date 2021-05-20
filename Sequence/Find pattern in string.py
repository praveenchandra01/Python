x=input("Enter the string :")
a=input("Enter the parttern :")
y=x.count(a)
if a in x:
        print("Pattern found")
else:
        print("Pattern not found")

print("Occurence of",a,"is",y)
input()
