def String(a):
    return ' , '.join(a) 
def Permute(s,i,n):
    if i==n:
        print(String(s))
    else:
        for j in range(i,n+1):
            s[i],s[j]=s[j],s[i]
            Permute(s,i+1,n)
            s[i],s[j]=s[j],s[i]
N=input("Enter String :")
l=len(N)
S=list(N)
Permute(S,0,l-1)
input()
