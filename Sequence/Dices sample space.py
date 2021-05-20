s1={1,2,3,4,5,6}
s2={1,2,3,4,5,6}
N=int(input("Enter the value of sum :"))
product=[]
for i in s1:
    for j in s2:
        if i+j==N:
            product.append([i,j])
print(product)
input()
            
