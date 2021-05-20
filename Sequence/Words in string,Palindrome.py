x=input("Enter string :")
y=x.split()
z=len(y)
y.sort()
print("word in this string :",z)
print("Sorted String :")
for i in y:
    print(i)
print("Sorted sentence: "," ".join(y))
print("***String Palindrome***")
a=x[::-1]
if a==x:
    print("String is Palindrome")
else:
    print("String is not a Palindrome")
input()
