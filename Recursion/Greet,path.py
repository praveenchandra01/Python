i=0
def Greet():
     global i
     i+=1   
     print("Hello",i)
     Greet()
def path(m,n):
     if m==1 or n==1:
          return 1
     else:
          return path(n,m-1) + path(m,n-1)
#Greet()    
r=path(200,1)
print(r)
input()
