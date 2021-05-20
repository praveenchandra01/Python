d={x:input("Enter values in dictionary :") for x in range(1,5)}
print(d)
for i in d:
    print(i,':',d[i])

d={int(input("Enter key :")):int(input("Enter Value :")) for x in range(1,3)}
print(d)
s=0
for i in d:
    s=s+d[i]
print("Sum of values :",s)    
input()
