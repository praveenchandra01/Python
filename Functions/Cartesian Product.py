def combination(x):
    product=[]
    for i in x:
        for j in x:
            product.append((i,j))
    return product        
s=set([eval(e) for e in input("Enter the elements in set :").split(',')])
r=combination(s)
print(r)
input()
