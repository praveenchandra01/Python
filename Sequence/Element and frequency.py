l=[]
print("Enter elements in the list :")
for i in range(5):
        x=int(input())
        l.append(x)
print(l)
'''l=eval(input("Enter element in list"))'''
i=0
while i<len(l):
    a=l.count(l[i])
    print("Index :",i,"Element :",l[i],"Frequency :",a)
    i+=1
a=0
print("Element - index")
for e in l:
      if a==l.index(e):
              print(e,'    -    ',l.count(e))
      a+=1        
input()
