f=open('File1.txt','w')
text=input("Enter some text :")
f.write(text)
f.close()

f=open('File1.txt','w')
l=['Bhopal\n','Indore\n','Delhi\n','jaipur']
f.writelines(l)
f.close()

f=open('File1.txt','r')
for lines in f:
    print(lines)
s=f.read(5)
s1=f.read(5)
print(s)
print(s1)
f.close()

 
input()
