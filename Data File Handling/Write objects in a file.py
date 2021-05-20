class students:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
students_list=[students("Amit",19),students("Rahil",20),students("Ramesh",18),students("Ajay",19)]

def savestudents():
    import pickle
    f1=open('file.obj','wb')
    for s in students_list:
        pickle.dump(s,f1) #(jo write karna hai,file pointer jisme write karna h)
    f1.close()
    
def viewStudent():
    import pickle
    f2=open("file.obj",'rb')
    s_list=[]
    while True:
        try:
            s_list+=[pickle.load(f2)]
        except EOFError:
                break
    print(s_list)
    return s_list

savestudents()
l=viewStudent()

for i in l:
    print("Name",i.name,".....","Age",i.age)
