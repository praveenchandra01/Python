f=open('File1.txt','r')
s=f.readlines()  #returns data of file in term of list
print(s)
x=input("Enter name of your city :")
x+='\n'
for e in s:
    if e==x:
        print("Matched City name is ",x)
f.close()
input()
