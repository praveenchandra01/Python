'''from sys import argv
for x in argv :
    print(x,type(x))'''

from sys import argv
y=0
s=0
for x in argv:
    if y==0:
        y=1
    else :
        s=s+int(x)
print(s)
input()




'''Run through cmd promt'''
