s1=[e for e in input("Enter elements in set :").split(',')]
p=2**len(s1)
print("No. of subsets in power set :",p)
powerset=[]
for i in range(p):
    subset=[]
    for j in range(len(s1)):
        if i&(1<<j):
            subset.append(s1[j])
    powerset.append(subset)
print(powerset)    
input()
