def avg(a,b):
    return (a+b)/2
x=avg(10,20)
print("Averege is ",x)

def avg(*n):
    print(n,type(n))
    return n
x=avg(10,20,30)

def f1(*points,playername):
    print(playername,end=' ')
    s=0
    for x in points:
        s=s+x
    print('Total points :',s)
f1(10,20,30,playername="ajay")#player name =keyword argument
f1(12,20,30,playername='aman')


def f1(**k):
    print("Person Information")
    for key,values in k.items():
        print(key," - ",values)
f1(Name='sameer',age=22)
f1(Name='rahul',marks=87,age=23)
f1(Name='ajay',emipd=125,salary=35000.00)
input()
