chance=1
while chance<=3 :
       x=int(input("Enter a even number :"))
       if x%2==0 :
            break
       chance+=1

if chance==4 :
    print("You loose")
else :
    print("You win") 

'''Print numbers 1 to 24 skipping multiples of 5'''

x=1
while x<=24 :
    
    if x%5==0:
        x+=1
        continue
        
    print(x)   
    x+=1
   
    

y=0
if y==0:
    pass
print("Done")

input()
