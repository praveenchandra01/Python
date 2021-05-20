class Book:
    def __init__(self,x,y,z,a,b):
        self.name=x
        self.Bookid=y
        self.Price=z
        self.Author=a
        self.Publisher=b
        print("\n")
        
    @staticmethod
    def Sort_list(l):
        l.sort(key=lambda x : x.name)
        print("Sort_name")
        for i in range(3):
            print("Name :",l[i].name,", Book ID :",l[i].Bookid,", Price :",l[i].Price,", Author :",l[i].Author,", Publisher :",l[i].Publisher)

            
    @staticmethod
    def Sort_list_P(l):
        l.sort(key=lambda x : x.Price)
        print("\nSort_price")
        for i in range(3):
            print("Name :",l[i].name,", Book ID :",l[i].Bookid,", Price :",l[i].Price,", Author :",l[i].Author,", Publisher :",l[i].Publisher)
                    
l=[] #Executuon starts fom here
for i in range(3):
    n=input("Enter Book Name :")
    bid=int(input("EnterBook ID :"))
    r=int(input("Enter the Price of Book :"))
    a=input("Enter Author :")
    p=input("Enter Publisher :")
    l.append(Book(n,bid,r,a,p))
Book.Sort_list(l)
Book.Sort_list_P(l)
input()