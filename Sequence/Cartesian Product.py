s1=[eval(e) for e in input("Enter elements in set 1:").split(',')]
s2=[eval(e) for e in input("Enter elements in set 2 :").split(',')]
product=[]
for i in s1:
    for j in s2:
         product.append([i,j])
print(product)         
input()
