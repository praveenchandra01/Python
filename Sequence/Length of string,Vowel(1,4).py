x=input("Enter string :")
y=len(x)
print("Length of string is :",y)
count=0
for i in x:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        count+=1
print("Vowels in the string is :",count)        
print("String in reverse order :",x[y:  :-1])
e=input("Enter character to find its frequency :")
w=0
for i in x:
    if i==e:
        w+=1
a=x.count(e)
d=0
s=0
while d<len(x):
    if e==x[d]:
        s=s+1
    d+=1 
print(a,w,s,sep=':')
input()
