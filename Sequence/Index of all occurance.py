l=[]
'''n=int(input("enter the lenght of list"))'''
print("Enter elements in the list :")
for i in range(5):
        x=int(input())
        l.append(x)
print(l)
i=0
Element=int(input("Enter the element to find its indices :"))
while  i<len(l):
    if l[i]==Element:
        print(i,end=' ')
    i+=1
print("\n Element=",l[x])
for x in range(len(l)):
     if l[x]==Element:
  
        print("index=",x)
input()
