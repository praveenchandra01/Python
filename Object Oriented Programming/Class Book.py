class Book:
    def Get_data(self):
        self.name=input("Enter Book Name :")
        self.Bookid=int(input("Enter Book ID :"))
        self.Price=int(input("Enter the Price of Book :"))
        self.Author=input("Enter Author name :")
        self.Publisher=input("Enter Publisher name :") 
        print("\n")

    def Show_data(self):
        print("Book Name :",self.name)
        print("Book ID :",self.Bookid)
        print("Book Price :",self.Price)
        print("Book Author :",self.Author)
        print("Book Publisher :",self.Publisher)
        print("\n")

    def Change_price(self):
        self.Price=int(input("Enter New Price of thr Book :"))
        print("Book Name :",self.name)
        print("Book ID :",self.Bookid)
        print("New Price :",self.Price)
        print("Book Author :",self.Author)
        print("Book Publisher :",self.Publisher)
        print("\n")

   
B1=Book()
B1.Get_data()
B1.Show_data()
B1.Change_price()
input()

