f=open('File1.txt','r+')
x='Indore\n'
s=f.readline()
l=0
while True:
    if s==' ':
        break
    l+=len(s)
    if s==x:
        f.seek(l-len(s)+1,0) #(14-7+1 toltal - current string,0=from begn. ,1=from current pos of coursor, 2=at last)
        f.write("INDORE\n")
        break
    s=f.readline()
f.close()    
