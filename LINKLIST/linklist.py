class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.start=None


    def viewlist(self):
        if self.start==None:
            print("list is empty")
        else:
            temp=self.start
            while temp!=None:
                print(temp.data,end="")
                temp=temp.next

    def deletefirst(self):
        if self.start==None:
            print("linkedlist is empty")
        else:
        #    temp=self.start
           self.start==self.start.next 

    
    
    def insertlast(self,value):
        newNode=node(value)
        if (self.start==None):
            self.start=newNode
        else:
            temp=self.start 
            while temp.next!=None:
                temp=temp.next
            temp.next=newNode

mylist=linkedlist()
mylist.insert(10)  
mylist.viewlist()
print()
mylist.deletefirst()
mylist.viewlist()

    