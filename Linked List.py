class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList :
    def __init__(self):
        self.start=None
        
    def insertLast(self,value):
        NewNode=node(value)
        if self.start==None:
            self.start=NewNode
        else:
            temp=self.start
            while temp.next!=None :
                temp=temp.next
            temp.next=NewNode

    def deleteFirst(self):
        if self.start==None:
            print("Linked list is empty")
        else:
            self.start=self.start.next
            
    def viewList(self):
        if self.start==None :
            print("Linked list is empty")
        else:
            temp=self.start
            while temp.next!=None:
                print(temp.data,end=' ')
                temp=temp.next

print("Linked List Created")
myList=LinkedList()
myList.insertLast(10)
myList.insertLast(20)
myList.insertLast(30)
myList.insertLast(40)
myList.insertLast(50)
myList.viewList()
myList.deleteFirst()
print()
print("Linked List after deletion")
myList.viewList()
input()