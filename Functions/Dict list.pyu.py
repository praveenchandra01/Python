def Dict_ls(x):
    d={}
    for i in x:
        print("Enter the word starting with",i)
        d[i]=input()
    return d
l=['A','B','C','D']
r=Dict_ls(l)
print(r)
input()
