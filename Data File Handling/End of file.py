'#End of File
'''
f=open('File1.txt','r')
s1=f.readline()
print(s1)
s1=f.readline()
print(s1)
s1=f.readline()
print(s1)
s1=f.readline()
print(s1)
s1=f.readline()
print(s1)'''


f=open('File1.txt','r')
while True:
    s1=f.readline()
    if s1=='':
        break
    print(s1)
print("Outside while loop")    
f.close()    
input()
