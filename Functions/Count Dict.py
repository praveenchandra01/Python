def count_dict(x):
    d={}
    for i in x:
        d[i]=x.count(i)
    return d    
t=(1,2,1,2,3,5,4,5)
r=count_dict(t)
print(r)
input()
