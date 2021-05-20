n=int(input("Enter a number to wheather it is palindrome or not :"))
temp=n
d=0
while n!=0:
    r=n%10
    d=d*10+r
    n=n//10
print(d)    
if temp==d:
    print("Number is Palindrome")
else:
    print("Number is not palindrome")
input()
