print("Enter the city names")
a,b,c=input(),input(),input()
'''if a<b<c :
    print(a,b,c)
elif a<c<b :
    print(a,c,b)
elif b<a<c :
    print(b,a,c)
elif b<c<a :
    print (b,c,a)
elif c<a<b :
    print (c,a,b)
else :
    print(c,b,a)'''
y=min(a,b,c)
print(y)
if y==a :
    print(min(b,c),"\n",max(b,c))
elif y==b  :  
    print(min(a,c),"\n",max(a,c))
else :
    print(min(a,b),"\n",max(a,b))
input()    


    
