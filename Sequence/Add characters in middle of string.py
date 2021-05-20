def repeatchar(s,c,n):
    l=int(len(s)/2)
    for i in range(n):
        s=s[:l] + c + s[l:]
    return s 

s=input("Enter string : ")
c=input("Enter char : ")
n=int(input("Enter reps : "))
p=repeatchar(s,c,n)
print(p)
input()
